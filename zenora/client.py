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

from zenora.exceptions import AuthenticationError, BadTokenError
from zenora import UserAPI, OauthAPI, UserAPIImpl, OauthAPIImpl
from typing import Final, List, Optional


__all__: Final[List[str]] = ["APIClient"]


class APIClient:
    """The API client for accessing the Discord REST API

    Args:
        token (str): Token for the bot/user
        validate_token (bool, optional): Whether the token should be validated during API instantiation. Defaults to True.
        client_secret (str, optional): Client secret for bot, especially if you are using Oauth. Defaults to None.
        bearer (bool, optional): Enable bearer tokens, necessary when you are using Oauth. Defaults to False.
    """

    def __init__(
        self,
        token: str,
        *,
        validate_token: bool = True,
        client_secret: Optional[str] = None,
        bearer: Optional[bool] = False,
    ) -> None:
        self._token_prefix = "Bot" if not bearer else "Bearer"
        self._token = f"{self._token_prefix} {token}"
        self._client_secret = client_secret
        self._user_client = UserAPIImpl(self)
        self._oauth_client = None

        if client_secret:
            self._oauth_client = OauthAPIImpl(self, client_secret)

        if validate_token:
            self._validate_token()

    def _validate_token(self) -> None:
        try:
            self.users.get_current_user()
        except AuthenticationError:
            raise BadTokenError("Invalid token has been passed")

    def set_token(self, token: str) -> None:
        """Sets the token for the API client instance"""
        self._token = f"{self._token_prefix} {token}"
        self._validate_token()

    @property
    def users(self) -> UserAPI:
        """Returns an instance of the UserAPI class"""
        return self._user_client

    @property
    def oauth(self) -> Optional[OauthAPI]:
        """Returns an instance of the OauthAPI class"""
        return self._oauth_client
