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

from zenora import Snowflake, User

import attr
import typing

__all__: typing.Final[typing.List[str]] = ["Integration"]


@attr.s(slots=True)
class IntegrationAccount:
    id: str = attr.ib()
    name: str = attr.ib()


@attr.s(slots=True)
class Integration:
    """An object representing a server integration"""

    """ID of the integration"""
    id: Snowflake = attr.ib(converter=Snowflake)

    """Name of the integration"""
    name: str = attr.ib(kw_only=True)

    """Type of the integration"""
    type: str = attr.ib()

    _enabled: bool = attr.ib()

    """ID of the role that this integration uses"""
    role_id: Snowflake = attr.ib(default=None)

    """Whether emoticons should be synced for this integration (Twitch only currently)"""
    enable_emoticons: typing.Optional[bool] = attr.ib(default=None)

    """The behaviour of expiring subscribers"""
    expire_behaviour: typing.Optional[typing.Literal[0, 1]] = attr.ib(
        default=None
    )

    """The grace period (in days) before expiring subscribers"""
    expire_grace_period: typing.Optional[int] = attr.ib(default=None)

    """User for this integration"""
    user: typing.Optional[User] = attr.ib(default=None)

    """Integration account information"""
    account: typing.Optional[IntegrationAccount] = attr.ib(
        default=None, converter=IntegrationAccount
    )

    """Last synced at (ISO8601 timestamp)"""
    synced_at: typing.Optional[str] = attr.ib(default=None)

    """How many subscribers this integration has"""
    subscriber_count: typing.Optional[int] = attr.ib(default=None)

    """Bot application for Integrations"""
    application: typing.Optional[dict] = attr.ib(default=None)

    _syncing: typing.Optional[bool] = attr.ib(default=None)

    _revoked: typing.Optional[bool] = attr.ib(default=None)

    @property
    def is_enabled(self) -> bool:
        """Whether the integration is enabled"""
        return self._enabled

    @property
    def is_syncing(self) -> typing.Optional[bool]:
        """Whether the integration is syncing"""
        return self._syncing

    @property
    def is_revoked(self) -> typing.Optional[bool]:
        """Has this integration been revoked"""
        return self._revoked
