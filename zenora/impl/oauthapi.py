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

from zenora import OauthAPI
from zenora.request import Request
from zenora.routes import BASE_URL, OAUTH_TOKEN_URL
from ..models.oauth import OauthResponse

import typing


__all__: typing.Final[typing.List[str]] = ["OauthAPIImpl"]


class OauthAPIImpl(OauthAPI):
    def __init__(self, app, client_secret):
        self._app = app
        self._token = app._token
        self._client_secret = client_secret

    def get_access_token(
        self, code: str, redirect_uri: str
    ) -> typing.Optional[OauthResponse]:
        url = BASE_URL + OAUTH_TOKEN_URL

        current_user = self._app.users.get_current_user()

        data = {
            "client_id": current_user.id,
            "client_secret": self._client_secret,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri,
            "code": code,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        request = Request(
            self._token, url, "POST", form_data=data, headers=headers
        )
        payload = request.execute()
        return OauthResponse(**payload)

    def refresh_access_token(
        self, refresh_token: str
    ) -> typing.Optional[OauthResponse]:
        url = BASE_URL + OAUTH_TOKEN_URL

        current_user = self._app.users.get_current_user()

        data = {
            "client_id": current_user.id,
            "client_secret": self._client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        request = Request(
            self._token, url, "POST", form_data=data, headers=headers
        )
        payload = request.execute()
        return OauthResponse(**payload)
