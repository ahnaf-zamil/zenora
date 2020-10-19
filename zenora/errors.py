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

class APIError(Exception):
    """Raised when user/bot does something unexpected that's not compliant with the Discord API.

    :type Exception: zenora.errors.MissingAccess
    """

    pass

class MissingAccess(Exception):
    """Raised when user/bot does not have access to specified channel.

    :type Exception: zenora.errors.MissingAccess
    """

    pass


class InvalidUser(Exception):
    """Raised when user with specified snowflake does not exist.

    :type Exception: zenora.errors.InvalidUser
    """

    pass


class InvalidSnowflake(Exception):
    """Raised when snowflake ID for accessing API is not valid.

    :type Exception: zenora.errors.InvalidSnowflake
    """

    pass


class AvatarError(Exception):
    """Raised when current user is changing avatar very fast.

    :type Exception: zenora.errors.AvatarError
    """

    pass


class GuildError(Exception):
    """Raised when the specified guild is either invalid or the user doesn't have access to it.

    :type Exception: zenora.errors.GuildError
    """

    pass
