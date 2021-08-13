# Copyright (c) 2021 DevGuyAhnaf

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

from zenora.utils import convert_image_to_data, extract_snowflake_from_object
from zenora.routes import (
    BASE_URL,
    GET_CURRENT_USER,
    GET_USER,
    GET_USER_CONNECTIONS,
    DM_URL,
)
from zenora.request import Request
from zenora import OwnUser, User, Snowflake, Connection, UserAPI, SnowflakeOr

import typing

__all__: typing.Final[typing.List[str]] = ["UserAPIImpl"]


class UserAPIImpl(UserAPI):
    _token: str

    def __init__(self, app):
        self._token = app._token
        self._app = app

    def get_current_user(self) -> OwnUser:
        url = BASE_URL + GET_CURRENT_USER
        request = Request(self._token, url, "GET")
        payload = request.execute()
        return OwnUser(**payload)

    def get_user(self, user_id: typing.Union[str, Snowflake]) -> User:
        url = BASE_URL + GET_USER.format(user_id)
        request = Request(self._token, url, "GET")
        payload = request.execute()
        return User(**payload)

    def modify_current_user(
        self,
        username: str = None,
        avatar=None,
    ) -> OwnUser:
        url = BASE_URL + GET_CURRENT_USER

        json_payload = {}

        if username:
            json_payload["username"] = username
        if avatar:
            json_payload["avatar"] = convert_image_to_data(avatar)

        request = Request(self._token, url, "PATCH", json_data=json_payload)
        payload = request.execute()
        if "token" in payload:
            self._token = self._app._token = payload["token"]
            del payload["token"]
        return OwnUser(**payload)

    def get_current_user_connections(self) -> typing.List[Connection]:
        url = BASE_URL + GET_USER_CONNECTIONS

        request = Request(self._token, url, "GET")
        payload = request.execute()

        return_data = []
        for x in payload:
            return_data.append(Connection(**x))

        return return_data

    def create_dm(self, user: typing.Union[SnowflakeOr, User]) -> dict:
        url = BASE_URL + DM_URL
        request = Request(
            self._token,
            url,
            "POST",
            json_data={"recipient_id": extract_snowflake_from_object(user)},
        )
        payload = request.execute()

        return payload
