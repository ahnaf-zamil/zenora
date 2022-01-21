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

from zenora.deserializers import deserialize_server_integration
from zenora.utils import get__str__
from .integration import Integration  # type: ignore[attr-defined]
from typing import Final, List, Literal, Optional

import attr


__all__: Final[List[str]] = ["Connection"]


@attr.s(slots=True)
class Connection:
    """An object representing a user's connection on Discord e.g YouTube, Facebook, Steam, etc."""

    __str__ = get__str__

    id: str = attr.ib()
    """ID of the connection account"""

    name: str = attr.ib()
    """The username of the connection account"""

    type: str = attr.ib()
    """The service type of the connection e.g YouTube, Facebook, Steam, etc."""

    visibility: Literal[0, 1] = attr.ib()
    """Visibility of the connection. 0 = False, 1 = True"""

    integrations: Optional[List[Integration]] = attr.ib(  # type: ignore[misc]
        default=None, converter=deserialize_server_integration
    )
    """Array of partial server integrations"""

    access_token: Optional[str] = attr.ib(default=None)
    """Access token for the integration"""

    _verified: Optional[bool] = attr.ib(default=None)

    _revoked: Optional[bool] = attr.ib(default=None)

    _friend_sync: Optional[bool] = attr.ib(default=None)

    _show_activity: Optional[bool] = attr.ib(default=None)

    @property
    def is_verified(self) -> Optional[bool]:
        """Whether the connection is verified"""
        return self._verified

    @property
    def is_revoked(self) -> Optional[bool]:
        """Whether the connection is revoked"""
        return self._revoked

    @property
    def has_friend_sync(self) -> Optional[bool]:
        """Whether friend sync is enabled for this connection"""
        return self._friend_sync

    @property
    def shows_activity(self) -> Optional[bool]:
        """Whether activities related to this connection will be shown in presence updates"""
        return self._show_activity
