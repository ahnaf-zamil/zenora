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

from zenora.utils import get__str__
from zenora.routes import CDN_URL, GUILD_ICON
from zenora import Snowflake
from zenora.models.snowflake import convert_snowflake
from typing import Final, Optional, List, Literal

import attr

__all__: Final[List[str]] = [
    "GuildPreview",
    "GuildOptional",
    "Guild",
    "GuildBase",
]


@attr.s(slots=True, kw_only=True)
class GuildBase:
    __str__ = get__str__

    id: Snowflake = attr.ib(converter=convert_snowflake)
    """ID of the guild"""

    unavailable: bool = attr.ib(default=False)
    """Whether the guild is unavailable or not"""


@attr.s(slots=True)
class GuildPreview(GuildBase):
    name: str = attr.ib()
    """The guild's name"""

    features: List[str] = attr.ib()
    """A list of guild features, dont have a model at the moment"""

    emojis: List[dict] = attr.ib(default=[])
    """A list of guild emojis, dont have a model at the moment"""

    description: Optional[str] = attr.ib(default=None)
    """The guild's description"""

    vanity_url_code: Optional[str] = attr.ib(default=None)
    """The vanity url code for the guild"""

    icon: Optional[str] = attr.ib(default=None)
    """The guild's icon image hash"""

    splash: Optional[str] = attr.ib(default=None)
    """The guild's splash image hash"""

    discovery_splash: Optional[str] = attr.ib(default=None)
    """The guild's discovery splash image hash"""

    @property
    def icon_url(self) -> Optional[str]:
        """Returns the user's avatar URL, only if the avatar hash exists"""
        if not self.icon:
            return None

        return f"{CDN_URL}{GUILD_ICON}/{self.id}/{self.icon}.png"

    def icon_url_as(
        self,
        format: Literal[".png", ".jpg", ".jpeg", ".webp", ".gif"] = ".png",
        size: int = 1024,
    ) -> Optional[str]:
        """Returns the guild's icon URL with a specific file format, only if the icon hash exists"""
        if not self.icon:
            return None
        elif format not in [".png", ".jpg", ".jpeg", ".webp", ".gif"]:
            raise Exception(f"Invalid avatar format: {format}")
        elif size % 16 != 0 or size > 1024:
            raise Exception(
                f"Invalid size {size}. Guild icon URL size must be a multiple of 16 up to 1024"
            )

        return (
            f"{CDN_URL}{GUILD_ICON}/{self.id}/{self.icon}{format}?size={size}"
        )


@attr.s
class GuildOptional:
    owner: Optional[bool] = attr.ib(default=None)
    """Whether the user is the guild's owner or not"""

    joined_at: Optional[str] = attr.ib(default=None)
    """ISO8601 timestamp for when the user joined the guild"""

    permissions: Optional[str] = attr.ib(default=None)
    """Total permissions for the user in the guild"""

    member_count: Optional[int] = attr.ib(default=None)
    """Total number of members in the guild"""

    widget_enabled: Optional[bool] = attr.ib(default=None)
    """Whether the server widget is enabled or not"""

    widget_channel_id: Optional[Snowflake] = attr.ib(
        default=None, converter=convert_snowflake
    )
    """The server widget's channel ID"""

    large: Optional[bool] = attr.ib(default=None)
    """Whether the guild is "large" or not"""

    members: Optional[List[dict]] = attr.ib(default=None)
    """A list of the guild's members, has no model at the moment"""

    channels: Optional[List[dict]] = attr.ib(default=None)
    """A list of the guild's channels, has no model at the moment"""

    threads: Optional[List[dict]] = attr.ib(default=None)
    """A list of the guild's threads, has no model at the moment"""

    presences: Optional[List[dict]] = attr.ib(default=None)
    """A list of partial presence update objects, has no model at the moment"""

    max_presences: Optional[int] = attr.ib(default=None)
    """The maximum number of presences for the guild"""

    max_members: Optional[int] = attr.ib(default=None)
    """The maximum number of members for the guild"""

    @property
    def is_owner(self) -> Optional[bool]:
        """Whether the user is the guild's owner or not"""
        return self.owner


@attr.s(slots=True, kw_only=True)
class Guild(GuildPreview, GuildOptional):
    """An object representing a guild/server on Discord"""

    owner_id: Optional[Snowflake] = attr.ib(
        default=None, converter=convert_snowflake
    )
    """The guild owner's ID"""

    region: Optional[str] = attr.ib(default=None)
    """The guild's voice server region"""

    roles: Optional[List[dict]] = attr.ib(default=None)
    """A list of guild role objects, dont have a model at the moment"""

    verification_level: Optional[Literal[0, 1, 2, 3, 4]] = attr.ib(default=None)
    """The guild's verification level"""

    nsfw_level: Optional[Literal[0, 1, 2, 3]] = attr.ib(default=None)
    """The guild's NSFW level"""

    mfa_level: Optional[Literal[0, 1]] = attr.ib(default=None)
    """The guild's multi-factor authentication level"""
