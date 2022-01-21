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

from typing import Final, List

import attr


__all__: Final[List[str]] = ["OauthResponse"]


@attr.s(slots=True)
class OauthResponse:
    """An object representing an Oauth API response from the Discord API"""

    access_token: str = attr.ib()
    """The access token returned by the API"""

    token_type: str = attr.ib()
    """Type of the token"""

    scope: str = attr.ib()
    """Oauth scopes for which the token has been provided"""

    expires_in: int = attr.ib(default=None)
    """Amount of time it expires after"""

    refresh_token: str = attr.ib(default=None)
    """A refresh token for getting another token just in case the current one expires"""
