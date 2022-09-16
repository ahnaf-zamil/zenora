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
from zenora.exceptions import APIError, RateLimitException, AuthenticationError
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


def test_handle_request_err():
    with mock.patch.object(requests, "request") as r:
        # Exception should be raised
        r.return_value.ok = False
        r.return_value.json.return_value = {
            "code": 50035,
            "message": "Invalid Form Body",
            "errors": {
                "_errors": [
                    {
                        "code": "APPLICATION_COMMAND_TOO_LARGE",
                        "message": "Command exceeds maximum size (4000)",
                    }
                ]
            },
        }
        with pytest.raises(APIError) as e:
            raise_error_or_return(r())
            assert e.message == "Invalid form body"


def test_handle_array_err():
    with mock.patch.object(requests, "request") as r:
        # Exception should be raised
        r.return_value.ok = False
        r.return_value.json.return_value = {
            "code": 50035,
            "errors": {
                "activities": {
                    "0": {
                        "platform": {
                            "_errors": [
                                {
                                    "code": "BASE_TYPE_CHOICES",
                                    "message": "Value must be one of ('desktop', 'android', 'ios').",
                                }
                            ]
                        }
                    }
                }
            },
            "message": "Invalid Form Body",
        }
        with pytest.raises(APIError) as e:
            raise_error_or_return(r())
            assert e.message == "Invalid form body"


def test_handle_obj_err():
    with mock.patch.object(requests, "request") as r:
        # Exception should be raised
        r.return_value.ok = False
        r.return_value.json.return_value = {
            "code": 50035,
            "errors": {
                "access_token": {
                    "_errors": [
                        {
                            "code": "BASE_TYPE_REQUIRED",
                            "message": "This field is required",
                        }
                    ]
                }
            },
            "message": "Invalid Form Body",
        }
        with pytest.raises(APIError) as e:
            raise_error_or_return(r())
            assert e.message == "Invalid form body"


def test_oauth_invalid_client_err():
    with mock.patch.object(requests, "request") as r:
        # Exception should be raised
        r.return_value.ok = False
        r.return_value.status_code = 401
        r.return_value.json.return_value = {"error": "invalid_client"}
        with pytest.raises(AuthenticationError) as e:
            raise_error_or_return(r())
            assert e.message == "Invalid Client Secret has been passed"


def test_handle_no_err():
    with mock.patch.object(requests, "request") as r:
        # No error should be raised
        r.return_value.ok = True
        r.return_value.json.return_value = {"test": 123}
        json_data = raise_error_or_return(r())
        assert json_data == {"test": 123}
