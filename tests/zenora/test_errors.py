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

from unittest import mock
from zenora.exceptions import APIError, RateLimitException
from zenora.errors import raise_error_or_return

import pytest
import requests


def test_handle_rate_limit():
    with mock.patch.object(requests, "request") as r:
        # Should throw rate limit error
        r.return_value.headers = {
            "X-RateLimit-Remaining": 0,
            "X-RateLimit-Reset": 1470173023,
            "X-RateLimit-Reset-After": 1234.23414,
            "X-RateLimit-Bucket": "abcd1234",
        }
        r.return_value.ok = False
        r.return_value.json.return_value = {
            "message": "You are being rate limited.",
            "retry_after": 64.57,
            "global": True,
        }
        with pytest.raises(RateLimitException):
            raise_error_or_return(r())


def test_handle_error():
    with mock.patch.object(requests, "request") as r:
        # Exception should be raised
        r.return_value.ok = False
        r.return_value.json.return_value = {
            "code": 12345,
            "errors": {"avatar": [{"message": "Invalid form body"}]},
        }
        with pytest.raises(APIError) as e:
            raise_error_or_return(r())
            assert e.message == "Invalid form body"

        # No error should be raised
        r.return_value.ok = True
        r.return_value.json.return_value = {"test": 123}
        json_data = raise_error_or_return(r())
        assert json_data == {"test": 123}
