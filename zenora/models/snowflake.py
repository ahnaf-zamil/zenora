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

from datetime import datetime

import typing


__all__: typing.Final[typing.List[str]] = ["Snowflake", "SnowflakeOr"]


class Snowflake(int):
    """A unique ID for an entity on Discord e.g guild, user, role, channel, etc."""

    @property
    def timestamp(self) -> datetime:
        """Milliseconds since Discord Epoch, the first second of 2015 or 1420070400000."""
        return datetime.fromtimestamp(
            ((self >> 22) + 1420070400000) / 1000
        ).astimezone()

    @property
    def internal_worker_id(self) -> int:
        """ID of the worker which was responsible for the creation of this snowflake"""
        return (self & 0x3E0000) >> 17

    @property
    def internal_process_id(self) -> int:
        """ID of the process which generated this snowflake"""
        return (self & 0x1F000) >> 12

    @property
    def increment(self) -> int:
        """For every ID that is generated on that process, this number is incremented"""
        return self & 0xFFF


SnowflakeOr = typing.Union[Snowflake, int]
