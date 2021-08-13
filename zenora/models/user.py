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

from zenora.routes import CDN_URL, USER_AVATAR
from zenora.utils import get__str__
from zenora import Snowflake
import typing
import attr


__all__: typing.Final[typing.List[str]] = ["User", "OwnUser"]


@attr.s(slots=True)
class User:
    """An object representing a user on Discord"""

    __str__ = get__str__

    """A user's unique snowflake ID (in string format)"""
    id: Snowflake = attr.ib(converter=Snowflake)

    """The user's username, not unique across Discord"""
    username: str = attr.ib()

    """The user's 4 digit Discord tag"""
    discriminator: int = attr.ib()

    """The user's banner"""
    banner: str = attr.ib(default=None)

    """The user's banner colour"""
    banner_color: str = attr.ib(default=None)

    """The user's accent colour"""
    accent_color: str = attr.ib(default=None)

    """The user's public flags"""
    public_flags: typing.Optional[int] = attr.ib(default=None)

    """The user's bio"""
    bio: str = attr.ib(default=None)

    _avatar: typing.Optional[str] = attr.ib(default=None)

    _bot: typing.Optional[bool] = attr.ib(default=None)

    _system: typing.Optional[bool] = attr.ib(default=None)

    _mfa_enabled: typing.Optional[bool] = attr.ib(default=None)

    @property
    def avatar_hash(self) -> typing.Optional[str]:
        """The user's avatar hash"""
        return self._avatar

    @property
    def is_bot(self) -> typing.Optional[bool]:
        """Whether the user is a bot or human"""
        return self._bot

    @property
    def is_system(self) -> typing.Optional[bool]:
        """Whether the user is an Official Discord System user or not"""
        return self._system

    @property
    def has_mfa_enabled(self) -> typing.Optional[bool]:
        """Whether the user has two factor enabled on their account"""
        return self._mfa_enabled

    @property
    def avatar_url(self) -> typing.Optional[str]:
        """Returns the user's avatar URL, only if the avatar hash exists"""
        if not self._avatar:
            return None

        return f"{CDN_URL}{USER_AVATAR}/{self.id}/{self._avatar}.png"

    def avatar_url_as(
        self,
        format: typing.Literal[
            ".png", ".jpg", ".jpeg", ".webp", ".gif"
        ] = ".png",
        size: int = 1024,
    ) -> typing.Optional[str]:
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

    """The user's chosen language option"""
    locale: typing.Optional[str] = attr.ib(default=None)

    """The user's E-Mail"""
    email: typing.Optional[str] = attr.ib(default=None)

    """The user's flags"""
    flags: typing.Optional[int] = attr.ib(default=None)

    """The type of Discord Nitro subscription on a user's account"""
    premium_type: typing.Optional[int] = attr.ib(default=None)

    _verified: typing.Optional[bool] = attr.ib(default=None)

    @property
    def is_verified(self) -> typing.Optional[bool]:
        """Whether the E-Mail on this account has been verified"""
        return self._verified
