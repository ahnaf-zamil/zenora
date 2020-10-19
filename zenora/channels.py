# Zenora, a modern Python API wrapper for the Discord REST API
#
# Copyright (c) 2020 K.M Ahnaf Zamil
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import typing
from dataclasses import dataclass
import datetime
from .users import User
from zenora.messages import Message

@dataclass
class GuildTextChannel:

    """A server text channel object

    :return: Zenora Guild Text Channel object
    :rtype: zenora.GuildTextChannel
    """

    app: typing.Any
    id: int
    type: int = 0
    name: typing.Optional[str] = None
    position: typing.Optional[int] = None
    guild_id: typing.Optional[int] = None
    topic: typing.Optional[str] = None
    nsfw: typing.Optional[bool] = None
    last_message_id: typing.Optional[int] = None
    rate_limit_per_user: typing.Optional[datetime.timedelta] = None
    permission_overwrites: typing.Optional[typing.List[dict]] = None
    parent_id: typing.Optional[int] = None



    def get_message(self, id: int) -> typing.Optional[Message]:
        """Returns a channel message according to given ID."""

        return self.app.get_channel_message(channel_id=self.id, msg_id=id)

    def modify(self, **kwargs) -> typing.Any:
        """Modify this channel


        Parameters
        ----------
        args: typing.Dict
                A dictionary containing the changes to the current channel. Check this
                link for all the changes applicable https://discord.com/developers/docs/resources/channel#modify-channel

        Returns
        -------
        zenora.GuildTextChannel
                Zenora guild text channel object

        zenora.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.DMTextChannel
                Zenora DM text channel object
        """
        return self.app.modify_channel(self.id, kwargs)

    def delete(self) -> typing.Any:
        """Delete this channel"""
        return self.app.delete_channel(self.id)

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("name", self.name),
            ("position", self.position),
            ("nsfw", self.nsfw),
            ("permission_overwrites", self.permission_overwrites),
            ("parent_id", self.parent_id),
            ("guild_id", self.guild_id),
            ("topic", self.topic),
            ("last_message_id", self.last_message_id),
            ("rate_limit_per_user", self.rate_limit_per_user),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )

@dataclass
class DMTextChannel:
    """A DM/Private message text channel object


    :return: Zenora DM text channel object
    :rtype: zenora.DMTextChannel
    """
    
    app: typing.Any
    id: int
    type: int = 1
    recipients: typing.Optional[typing.List[User]] = None
    last_message_id: typing.Optional[int] = None

    def get_message(self, id: int) -> typing.Optional[Message]:
        """Returns a channel message according to given ID."""

        return self.app.get_channel_message(channel_id=self.id, msg_id=id)

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("last_message_id", self.last_message_id),
            ("recipients", self.recipients),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs if attrs is not None),
        )

@dataclass
class GuildVoiceChannel:
    """A guild voice channel object


    :return: Zenora guild voice channel object
    :rtype: zenora.GuildVoiceChannel
    """

    app: typing.Any
    id: int
    type: int = 2
    name: typing.Optional[str] = None
    position: typing.Optional[int] = None
    guild_id: typing.Optional[int] = None
    nsfw: typing.Optional[bool] = None
    bitrate: typing.Optional[int] = None
    user_limit: int = None
    permission_overwrites: typing.Optional[typing.List[dict]] = None
    parent_id: typing.Optional[int] = None

    def modify(self, **kwargs) -> typing.Any:
        """Modify this channel


        Parameters
        ----------
        args: typing.Dict
                A dictionary containing the changes to the current channel. Check this
                link for all the changes applicable https://discord.com/developers/docs/resources/channel#modify-channel

        Returns
        -------
        zenora.GuildTextChannel
                Zenora guild text channel object

        zenora.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.DMTextChannel
                Zenora DM text channel object
        """
        return self.app.modify_channel(self.id, kwargs)

    def delete(self) -> typing.Any:
        """Delete this channel"""
        return self.app.delete_channel(self.id)

    def __repr__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("name", self.name),
            ("position", self.position),
            ("is_nsfw", self.nsfw),
            ("permission_overwrites", self.permission_overwrites),
            ("category_id", self.parent_id),
            ("guild_id", self.guild_id),
            ("bitrate", self.bitrate),
            ("user_limit", self.user_limit),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )
