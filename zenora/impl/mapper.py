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
from zenora.channels import GuildTextChannel, GuildVoiceChannel, DMTextChannel
from zenora.base.mapper import ChannelMapper as BaseChannelMapper
from zenora.errors import MissingAccess
from zenora.base.mapper import BaseEmojiMapper
from zenora.emojis import Emoji


class ChannelMapper(BaseChannelMapper):
    def map(response, app) -> typing.Any:
        """Implementation of the channel mapper.

        Maps channel response to object according to channel type.

        Parameters
        ----------
        response: typing.Dict
                API response from Discord
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
        if "code" in response and response["code"] == 50001:
            raise MissingAccess("You don't have access to this channel")

        if response["type"] == 0:
            return GuildTextChannel(response, app)
        elif response["type"] == 1:
            return DMTextChannel(response, app)
        elif response["type"] == 2:
            return GuildVoiceChannel(response, app)


class EmojiMapper(BaseEmojiMapper):
    def map(response, app):
        """
        Implementation of the emoji mapper.

        Maps emoji response to object.

        Parameters
        ----------
        response: typing.Dict
                API response from Discord
        app: zenora.RESTAPI
                Zenora REST API object

        Returns
        -------
        zenora.emojis.Emoji
                Zenora emoji object
        """
        return Emoji(response, app)
