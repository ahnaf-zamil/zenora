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

from abc import abstractmethod, ABC
from zenora.models.oauth import OauthResponse

import typing


__all__: typing.Final[typing.List[str]] = ["OauthAPI"]


class OauthAPI(ABC):
    """A client for accessing Oauth features of the DIscord API"""

    @abstractmethod
    def get_access_token(
        self, code: str, redirect_uri: str
    ) -> typing.Optional[OauthResponse]:
        """Returns an access token using an Oauth code

        Returns:
            typing.Optional[OauthReponse]: An object containing Oauth data from the Discord API
        """

    @abstractmethod
    def refresh_access_token(
        self, refresh_token: str
    ) -> typing.Optional[OauthResponse]:
        """Refreshes the access token if it expires

        Returns:
            typing.Optional[OauthReponse]: An object containing Oauth data from the Discord API
        """
