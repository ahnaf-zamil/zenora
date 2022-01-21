# type: ignore[misc]

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

from zenora import Snowflake, User
from typing import Final, List, Optional, Literal
from zenora.models.snowflake import convert_snowflake

import attr

__all__: Final[List[str]] = [
    "Integration",
    "IntegrationAccount",
]


@attr.s(slots=True)
class IntegrationAccount:
    id: str = attr.ib()
    name: str = attr.ib()


@attr.s(slots=True)
class Integration:
    """An object representing a server integration"""

    _enabled: bool = attr.ib()

    id: Snowflake = attr.ib(converter=convert_snowflake)
    """ID of the integration"""

    name: str = attr.ib(kw_only=True)
    """Name of the integration"""

    type: str = attr.ib()
    """Type of the integration"""

    role_id: Snowflake = attr.ib(default=None)
    """ID of the role that this integration uses"""

    enable_emoticons: Optional[bool] = attr.ib(default=None)
    """Whether emoticons should be synced for this integration (Twitch only currently)"""

    expire_behaviour: Optional[Literal[0, 1]] = attr.ib(default=None)
    """The behaviour of expiring subscribers"""

    expire_grace_period: Optional[int] = attr.ib(default=None)
    """The grace period (in days) before expiring subscribers"""

    user: Optional[User] = attr.ib(default=None)
    """User for this integration"""

    account: Optional[IntegrationAccount] = attr.ib(
        default=None, converter=IntegrationAccount
    )
    """Integration account information"""

    synced_at: Optional[str] = attr.ib(default=None)
    """Last synced at (ISO8601 timestamp)"""

    subscriber_count: Optional[int] = attr.ib(default=None)
    """How many subscribers this integration has"""

    application: Optional[dict] = attr.ib(default=None)
    """Bot application for Integrations"""

    _syncing: Optional[bool] = attr.ib(default=None)

    _revoked: Optional[bool] = attr.ib(default=None)

    @property
    def is_enabled(self) -> bool:
        """Whether the integration is enabled"""
        return self._enabled

    @property
    def is_syncing(self) -> Optional[bool]:
        """Whether the integration is syncing"""
        return self._syncing

    @property
    def is_revoked(self) -> Optional[bool]:
        """Has this integration been revoked"""
        return self._revoked
