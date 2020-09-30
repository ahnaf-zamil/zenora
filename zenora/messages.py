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


class Message:
    """An object representing a Discord message"""

    __slots__ = ["data", "app"]

    def __init__(self, data: typing.Dict, app):
        self.data = data
        self.app = app

    @property
    def id(self):
        """The ID of the Discord message"""
        return int(self.data["id"])

    @property
    def type(self):
        """The type of message"""
        return int(self.data["type"])

    @property
    def content(self):
        """The message's content"""
        return self.data["content"]

    @property
    def channel(self):
        """A channel object representing the message's channel"""
        return self.app.get_channel(int(self.data["channel_id"]))

    @property
    def author(self):
        """A user object representing the message's author"""
        return self.app.get_user(int(self.data["author"]["id"]))

    @property
    def guild_id(self):
        """The guild ID of the message"""
        return int(self.channel.guild_id)

    @property
    def attachments(self):
        """Any attachments that came with the message"""
        return self.data["attachments"]

    @property
    def embeds(self):
        return self.data["embeds"]

    @property
    def mentions(self):
        """All of the mentions or pings in the message content"""
        return [self.app.get_user(i["id"]) for i in self.data["mentions"]]

    @property
    def mention_roles(self):
        """All of the roles mentioned in the message"""
        return self.data["mention_roles"]

    @property
    def pinned(self):
        """Whether the message is pinned or not"""
        return self.data["pinned"]

    @property
    def mention_everyone(self):
        """Whether the message has mentioned everyone in the server"""
        return self.data["mention_everyone"]

    @property
    def tts(self):
        """Checks if it's a text-to-speech message"""
        return self.data["tts"]

    @property
    def timestamp(self):
        """Timestamp of when the message was sent"""
        return self.data["timestamp"]

    @property
    def edited_timestamp(self):
        return self.data["edited_timestamp"]

    @property
    def flags(self):
        """Message flags"""
        return self.data["flags"]

    def __repr__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("type", self.type),
            ("content", self.content),
            ("channel", self.channel),
            ("guild_id", self.guild_id),
            ("author", self.author),
            ("attachments", self.attachments),
            ("embeds", self.embeds),
            ("mentions", self.mentions),
            ("metion_roles", self.mention_roles),
            ("pinned", self.pinned),
            ("mention_everyone", self.mention_everyone),
            ("tts", self.tts),
            ("timestamp", self.timestamp),
            ("edited_timestamp", self.edited_timestamp),
            ("flags", self.flags),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )
