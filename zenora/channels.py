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
import datetime
from zenora.users import User
from zenora.messages import Message


class GuildTextChannel:

    """A server text channel object

    :return: Zenora Guild Text Channel object
    :rtype: zenora.channels.GuildTextChannel
    """
    __slots__ = ["data", "app"]

    def __init__(self, data, app) -> None:
        self.data = data
        self.app = app

    @property
    def id(self) -> typing.Optional[int]:
        """Returns The snowflake ID of the channel."""
        return int(self.data["id"])

    @property
    def name(self) -> typing.Optional[str]:
        """Returns the name of the channel."""
        return self.data["name"]

    @property
    def position(self) -> typing.Optional[int]:
        """Returns the position of the channel."""
        return self.data["position"]

    @property
    def guild_id(self) -> typing.Optional[int]:
        """Returns the snowflake ID of the channel's guild."""
        return int(self.data["guild_id"])

    @property
    def topic(self) -> typing.Optional[str]:
        """Returns the topic of the channel."""
        return self.data["topic"]

    @property
    def is_nsfw(self) -> typing.Optional[bool]:
        """Returns if the channel is NSFW or not."""
        return self.data["nsfw"]

    @property
    def last_message_id(self) -> typing.Optional[int]:
        """Returns the snowflake ID of the last message of the channel."""
        return (
            int(self.data["last_message_id"])
            if self.data["last_message_id"] is not None
            else None
        )

    @property
    def rate_limit_per_user(self) -> datetime.timedelta:
        """Returns the rate limit per user of the channel."""
        return self.data["rate_limit_per_user"]

    @property
    def permission_overwrites(self) -> datetime.timedelta:
        """Returns the permission overwrites of the channel."""
        return self.data["permission_overwrites"]

    @property
    def category_id(self) -> datetime.timedelta:
        """Returns the snowflake ID of the parant category of the channel."""
        return (
            int(self.data["parent_id"])
            if self.data["parent_id"] is not None
            else None
        )

    def get_message(self, id: int) -> typing.Optional[Message]:
        """Returns a channel message according to given ID."""

        return self.app.get_channel_message(channel_id=self.id, msg_id=id)

    def modify(self, args) -> typing.Any:
        """Modify this channel


        Parameters
        ----------
        args: typing.Dict
                A dictionary containing the changes to the current channel. Check this
                link for all the changes applicable https://discord.com/developers/docs/resources/channel#modify-channel

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """
        return self.app.modify_channel(self.id, args)

    def delete(self) -> typing.Any:
        """Delete this channel"""
        return self.app.delete_channel(self.id)

    def __repr__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("name", self.name),
            ("position", self.position),
            ("is_nsfw", self.is_nsfw),
            ("permission_overwrites", self.permission_overwrites),
            ("category_id", self.category_id),
            ("guild_id", self.guild_id),
            ("topic", self.topic),
            ("last_message_id", self.last_message_id),
            ("rate_limit_per_user", self.rate_limit_per_user),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )


class DMTextChannel:
    """A DM/Private message text channel object


    :return: Zenora DM text channel object
    :rtype: zenora.channel.DMTextChannel
    """

    __slots__ = ["data", "app"]

    def __init__(self, data, app) -> None:
        self.data = data
        self.app = app

    @property
    def id(self) -> typing.Optional[int]:
        """Returns The snowflake ID of the channel."""
        return int(self.data["id"])

    @property
    def last_message_id(self) -> typing.Optional[int]:
        """Returns The last message ID of the channel."""
        return (
            int(self.data["last_message_id"])
            if self.data["last_message_id"] is not None
            else None
        )

    @property
    def recipients(self) -> typing.List[User]:
        """Returns The recipients of the channel.

        :return: List of Zenora partial user objects
        :rtype: typing.List[User]
        """
        return [User(i, self.app) for i in self.data["recipients"]]

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("last_message_id", self.last_message_id),
            ("recipients", self.recipients),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )


class GuildVoiceChannel:
    """A guild voice channel object


    :return: Zenora guild voice channel object
    :rtype: zenora.channel.GuildVoiceChannel
    """

    __slots__ = ["data"]

    def __init__(self, data) -> None:
        self.data = data

    @property
    def id(self) -> typing.Optional[int]:
        """Returns The snowflake ID of the channel."""
        return self.data["id"]

    @property
    def name(self) -> typing.Optional[str]:
        """Returns the name of the channel."""
        return self.data["name"]

    @property
    def position(self) -> typing.Optional[int]:
        """Returns the position of the channel."""
        return self.data["position"]

    @property
    def is_nsfw(self) -> typing.Optional[bool]:
        """Returns if the channel is NSFW or not."""
        return self.data["nsfw"]

    @property
    def bitrate(self) -> typing.Optional[int]:
        """Returns the bitrate of the channel."""
        return self.data["bitrate"]

    @property
    def user_limit(self) -> typing.Optional[int]:
        """Returns the user limit of the channel."""
        return self.data["nsfw"]

    @property
    def permission_overwrites(self) -> datetime.timedelta:
        """Returns the permission overwrites of the channel."""
        return self.data["permission_overwrites"]

    @property
    def guild_id(self) -> typing.Optional[int]:
        """Returns the snowflake ID of the channel's guild."""
        return int(self.data["guild_id"])

    @property
    def category_id(self) -> datetime.timedelta:
        """Returns the snowflake ID of the parant category of the channel."""
        return (
            int(self.data["parent_id"])
            if self.data["parent_id"] is not None
            else None
        )

    def modify(self, args) -> typing.Any:
        """Modify this channel


        Parameters
        ----------
        args: typing.Dict
                A dictionary containing the changes to the current channel. Check this
                link for all the changes applicable https://discord.com/developers/docs/resources/channel#modify-channel

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """
        return self.app.modify_channel(self.id, args)

    def delete(self) -> typing.Any:
        """Delete this channel"""
        return self.app.delete_channel(self.id)

    def __repr__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("name", self.name),
            ("position", self.position),
            ("is_nsfw", self.is_nsfw),
            ("permission_overwrites", self.permission_overwrites),
            ("category_id", self.category_id),
            ("guild_id", self.guild_id),
            ("bitrate", self.bitrate),
            ("user_limit", self.user_limit),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )
