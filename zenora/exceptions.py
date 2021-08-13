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

import typing


__all__: typing.Final[typing.List[str]] = [
    "ZenoraException",
    "APIError",
    "CloudflareException",
    "RateLimitException",
]


class ZenoraException(Exception):
    """Base exception for all Zenora exceptions"""


class APIError(ZenoraException):
    """Raised when an API error occurs"""


class CloudflareException(ZenoraException):
    """Raised when Cloudflare blocks any Zenora API requests (possibly due to rate limits)"""


class BadURLException(ZenoraException):
    """Raised when an invalid URL has been passed"""


class AuthenticationError(ZenoraException):
    """Raised when the Discord API responses with 401 status code"""


class BadTokenError(ZenoraException):
    """Raised when as invalid token is passed to the API constructor"""


class RateLimitException(ZenoraException):
    """Raised when rate limits are hit occurs"""

    def __init__(self, message, payload):
        super().__init__(message)
        self._payload = payload

    @property
    def ratelimit_limit(self) -> int:
        """The number of times a request can be made to this endpoint in a minute

        Returns:
            int: Number of times a request can be made to this endpoint in a minute
        """
        return self._payload["X-RateLimit-Limit"]

    @property
    def ratelimit_remaining(self) -> int:
        """The number of remaining requests that can be made

        Returns:
            int: Number of requests that can be made
        """
        return self._payload["X-RateLimit-Remaining"]

    @property
    def ratelimit_reset_after(self) -> float:
        """The total time (in seconds) of when the current rate limit bucket will reset

        Returns:
            float: Total time (in seconds) of when the current rate limit bucket will reset
        """
        return self._payload["X-RateLimit-Reset-After"]

    @property
    def ratelimit_bucket(self) -> str:
        """A unique string denoting the rate limit being encountered

        Returns:
            str: ID of the rate limit bucket
        """
        return self._payload["X-RateLimit-Bucket"]
