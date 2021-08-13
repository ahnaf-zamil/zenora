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

from zenora.models.oauth import OauthResponse
from unittest import mock

import pytest
import requests
import zenora


@pytest.fixture()
def api():
    return zenora.APIClient(
        "this token is so pog", validate_token=False, client_secret="asdsad"
    ).oauth


def test_get_access_token(api: zenora.OauthAPI):
    with mock.patch.object(zenora.UserAPIImpl, "get_current_user"):
        with mock.patch.object(requests, "request") as r:
            token_response = {
                "access_token": "asdsadsadasds",
                "token_type": "Bearer",
                "scope": "identify guilds email",
                "expires_in": 604800,
                "refresh_token": "dsadsadsadas",
            }

            r.return_value.status_code = 200
            r.return_value.json.return_value = token_response
            response = api.get_access_token(
                code="dsadasd", redirect_uri="dsadsadsadas"
            )
            r.assert_called_once()

            assert type(response) == OauthResponse
            assert response.refresh_token == token_response["refresh_token"]
            assert response.access_token == token_response["access_token"]
            assert response.scope == token_response["scope"]
            assert response.token_type == token_response["token_type"]


def test_get_refresh_token(api: zenora.OauthAPI):
    with mock.patch.object(zenora.UserAPIImpl, "get_current_user"):
        with mock.patch.object(requests, "request") as r:
            current_refresh_token = "abcdefg"
            token_response = {
                "access_token": "asdsadsadasds",
                "token_type": "Bearer",
                "scope": "identify guilds email",
                "expires_in": 604800,
                "refresh_token": "dsadsadsadas",
            }

            r.return_value.status_code = 200
            r.return_value.json.return_value = token_response
            response = api.refresh_access_token(
                refresh_token="current_refresh_token"
            )
            r.assert_called_once()

            assert type(response) == OauthResponse
            assert response.refresh_token != current_refresh_token
            assert response.scope == token_response["scope"]
            assert response.token_type == token_response["token_type"]
