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
from zenora.base.factory import Factory as BaseFactory
from zenora.impl.mapper import ChannelMapper, EmojiMapper
from zenora.messages import Message


class Factory(BaseFactory):
    def parse_channel(response: typing.Dict, app):
        """Parses response data from Dicord API into channel objects

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        app: zenora.RESTAPI
                Zenora REST API object

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """
        return ChannelMapper.map(response, app)

    def parse_user(response: typing.Dict, app):
        """Parses response data from Dicord API into user objects

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of the user

        Returns
        -------
        zenora.users.User
                Zenora user object
        """
        return User(response, app)

    def parse_emoji(response, app):
        """
        Parse response data from Dicord into Zenora's emoji object

        Parameters
        ----------
        response:
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of guild

        Returns
        -------
        zenora.emojis.Emoji
                Zenora emoji object

        """
        return EmojiMapper.map(response, app)

    def parse_message(response: typing.Dict, app) -> typing.Any:
        """Parses response data from Dicord API into message object
        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of the message
        Returns
        -------
        zenora.messages.Message
                Zenora message object
        """
        return Message(response, app)
