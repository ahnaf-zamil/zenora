# Copyright (c) 2022 DevGuyAhnaf

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from zenora.deserializers import deserialize_model
from zenora.utils import convert_image_to_data, extract_snowflake_from_object
from zenora.routes import (
    BASE_URL,
    GET_CURRENT_USER,
    GET_USER,
    GET_USER_CONNECTIONS,
    DM_URL,
    GET_USER_GUILDS,
)
from zenora.request import Request
from zenora import (
    OwnUser,
    User,
    Connection,
    UserAPI,
    SnowflakeOr,
    DMChannel,
    Guild,
)
from typing import List, Final, Optional

__all__: Final[List[str]] = ["UserAPIImpl"]


class UserAPIImpl(UserAPI):
    _token: str

    def __init__(self, app) -> None:  # type: ignore[no-untyped-def]
        self._token = app._token
        self._app = app

    def get_current_user(self) -> OwnUser:
        url = BASE_URL + GET_CURRENT_USER
        payload = Request.make_request(self._token, url, "GET")

        return deserialize_model(OwnUser, payload)

    def get_user(self, user_id: SnowflakeOr[str]) -> User:
        url = BASE_URL + GET_USER.format(user_id)
        payload = Request.make_request(self._token, url, "GET")
        return deserialize_model(User, payload)

    def modify_current_user(
        self,
        username: Optional[str] = None,
        avatar: Optional[str] = None,
    ) -> OwnUser:
        url = BASE_URL + GET_CURRENT_USER

        json_payload = {}

        if username:
            json_payload["username"] = username
        if avatar:
            json_payload["avatar"] = convert_image_to_data(avatar)

        payload = Request.make_request(
            self._token, url, "PATCH", json_data=json_payload
        )
        if "token" in payload:
            self._token = self._app._token = payload["token"]
            del payload["token"]
        return deserialize_model(OwnUser, payload)

    def get_current_user_connections(self) -> List[Connection]:
        url = BASE_URL + GET_USER_CONNECTIONS

        payload = Request.make_request(self._token, url, "GET")

        return_data: list = []
        for x in payload:
            return_data.append(deserialize_model(Connection, x))

        return return_data

    def create_dm(self, user: SnowflakeOr[User]) -> DMChannel:
        url = BASE_URL + DM_URL
        payload = Request.make_request(
            self._token,
            url,
            extract_snowflake_from_object(user),
        )

        return deserialize_model(DMChannel, payload)

    def get_my_guilds(self) -> List[Guild]:
        url = BASE_URL + GET_USER_GUILDS
        payload = Request.make_request(
            self._token,
            url,
            "GET",
        )
        return [deserialize_model(Guild, i) for i in payload]  # type: ignore[misc]
