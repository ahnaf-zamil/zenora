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


class Emoji:
    """A n emoji object


    :return: Zenora emoji object
    :rtype: zenora.Emoji
    """

    __slot__ = ["data", "app"]

    def __init__(self, data: typing.Dict, app):
        self.data = data
        self.app = app

    @property
    def id(self):
        """Snowflake ID of the emoji"""
        return int(self.data["id"])

    @property
    def name(self):
        """The emoji's name"""
        return self.data["name"]

    @property
    def roles(self):
        """The roles this emoji is whitelisted to"""
        return self.data["roles"] if "roles" in self.data else None

    @property
    def user(self):
        """The user that created this emoji"""
        return (
            self.app.get_user(int(self.data["user"]["id"]))
            if "user" in self.data
            else None
        )

    @property
    def require_colons(self):
        """Whether this emoji must be wrapped in colons"""
        return (
            self.data["require_colons"]
            if "require_colons" in self.data
            else None
        )

    @property
    def managed(self):
        """Whether this emoji is managed"""
        return self.data["managed"] if "managed" in self.data else None

    @property
    def animated(self):
        """Whether this emoji is animated"""
        return self.data["animated"] if "animated" in self.data else None

    def __repr__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("name", self.name),
            ("roles", self.roles),
            ("user", self.user),
            ("require_colons", self.require_colons),
            ("managed", self.managed),
            ("animated", self.animated),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )
