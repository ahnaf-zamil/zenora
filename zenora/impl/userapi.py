# Copyright (c) 2021 K.M Ahnaf Zamil

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

from zenora.routes import BASE_URL, GET_CURRENT_USER, GET_USER
from zenora.request import Request
from zenora import UserAPI, OwnUser, User, Snowflake

import typing

__all__: typing.Final[typing.List[str]] = ["UserAPIImpl"]


class UserAPIImpl(UserAPI):
    token: str

    def __init__(self, token: str):
        self.token = token

    def get_current_user(self) -> OwnUser:
        url = BASE_URL + GET_CURRENT_USER
        request = Request(self.token, url, "GET")
        payload = request.execute()
        return OwnUser(**payload)

    def get_user(self, user_id: typing.Union[str, Snowflake]) -> User:
        url = BASE_URL + GET_USER.format(user_id)
        request = Request(self.token, url, "GET")
        payload = request.execute()
        return User(**payload)
