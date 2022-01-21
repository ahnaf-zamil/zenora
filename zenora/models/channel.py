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
from zenora.utils import get__str__
from zenora.deserializers import deserialize_model
from typing import Final, List, Optional
from zenora.models.snowflake import convert_snowflake

import attr
import enum

__all__: Final[List[str]] = ["ChannelTypes", "DMChannel"]


class ChannelTypes(enum.Enum):
    """Enum for all Discord channel types"""

    GUILD_TEXT = 0
    """A text channel within a server"""

    DM = 1
    """A direct message between users"""

    GUILD_VOICE = 2
    """A voice channel within a server"""

    GROUP_DM = 3
    """A direct message between multiple users"""

    GUILD_CATEGORY = 4
    """An organizational category that contains up to 50 channels"""

    GUILD_NEWS = 5
    """A channel that users can follow and crosspost into their own server"""

    GUILD_STORE = 6
    """A channel in which game developers can sell their game on Discord"""

    GUILD_NEWS_THREAD = 10
    """A temporary sub-channel within a GUILD_NEWS channel"""

    GUILD_PUBLIC_THREAD = 11
    """A temporary sub-channel within a GUILD_TEXT channel"""

    GUILD_PRIVATE_THREAD = 12
    """A temporary sub-channel within a GUILD_TEXT channel that is only viewable by those invited and those with the 
    MANAGE_THREADS permission"""

    GUILD_STAGE_VOICE = 13
    """A  voice channel for hosting events with an audience"""


@attr.s(slots=True)
class BaseChannel:
    """Base class for all channel models"""

    __str__ = get__str__

    id: Snowflake = attr.ib(converter=convert_snowflake)
    """A user's unique snowflake ID (in string format)"""

    type: ChannelTypes = attr.ib(converter=ChannelTypes)
    """Type of the channel"""


@attr.s(slots=True)
class DMChannel(BaseChannel):
    """A model representing a DM/private channel on Discord"""

    last_message_id: Optional[Snowflake] = attr.ib()
    """Snowflake ID of the last message in the DM channel"""

    recipients: List[User] = attr.ib(
        converter=lambda x: [deserialize_model(User, i) for i in x]
    )
    """Recipients in the DM channel"""
