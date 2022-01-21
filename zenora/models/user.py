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

from zenora.routes import CDN_URL, USER_AVATAR
from zenora.utils import get__str__
from zenora import Snowflake
from typing import Optional, Final, List, Literal
from zenora.models.snowflake import convert_snowflake

import attr


__all__: Final[List[str]] = ["User", "OwnUser"]


@attr.s(slots=True)
class User:
    """An object representing a user on Discord"""

    __str__ = get__str__

    id: Snowflake = attr.ib(converter=convert_snowflake)
    """A user's unique snowflake ID (in string format)"""

    username: str = attr.ib()
    """The user's username, not unique across Discord"""

    discriminator: int = attr.ib()
    """The user's 4 digit Discord tag"""

    banner: str = attr.ib(default=None)
    """The user's banner"""

    banner_color: str = attr.ib(default=None)
    """The user's banner colour"""

    accent_color: str = attr.ib(default=None)
    """The user's accent colour"""

    public_flags: Optional[int] = attr.ib(default=None)
    """The user's public flags"""

    bio: str = attr.ib(default=None)
    """The user's bio"""

    _avatar: Optional[str] = attr.ib(default=None)

    _bot: Optional[bool] = attr.ib(default=None)

    _system: Optional[bool] = attr.ib(default=None)

    _mfa_enabled: Optional[bool] = attr.ib(default=None)

    @property
    def avatar_hash(self) -> Optional[str]:
        """The user's avatar hash"""
        return self._avatar

    @property
    def is_bot(self) -> Optional[bool]:
        """Whether the user is a bot or human"""
        return self._bot

    @property
    def is_system(self) -> Optional[bool]:
        """Whether the user is an Official Discord System user or not"""
        return self._system

    @property
    def has_mfa_enabled(self) -> Optional[bool]:
        """Whether the user has two factor enabled on their account"""
        return self._mfa_enabled

    @property
    def avatar_url(self) -> Optional[str]:
        """Returns the user's avatar URL, only if the avatar hash exists"""
        if not self._avatar:
            return None

        return f"{CDN_URL}{USER_AVATAR}/{self.id}/{self._avatar}.png"

    def avatar_url_as(
        self,
        format: Literal[".png", ".jpg", ".jpeg", ".webp", ".gif"] = ".png",
        size: int = 1024,
    ) -> Optional[str]:
        """Returns the user's avatar URL with a specific file format, only if the avatar hash exists"""
        if not self._avatar:
            return None
        elif format not in [".png", ".jpg", ".jpeg", ".webp", ".gif"]:
            raise Exception(f"Invalid avatar format: {format}")
        elif size % 16 != 0 or size > 1024:
            raise Exception(
                f"Invalid size {size}. Avatar URL size must be a multiple of 16 up to 1024"
            )

        return f"{CDN_URL}{USER_AVATAR}/{self.id}/{self._avatar}{format}?size={size}"


@attr.s(slots=True)
class OwnUser(User):
    """An object representing the current user on Discord"""

    locale: Optional[str] = attr.ib(default=None)
    """The user's chosen language option"""

    email: Optional[str] = attr.ib(default=None)
    """The user's E-Mail"""

    flags: Optional[int] = attr.ib(default=None)
    """The user's flags"""

    premium_type: Optional[int] = attr.ib(default=None)
    """The type of Discord Nitro subscription on a user's account"""

    _verified: Optional[bool] = attr.ib(default=None)

    @property
    def is_verified(self) -> Optional[bool]:
        """Whether the E-Mail on this account has been verified"""
        return self._verified
