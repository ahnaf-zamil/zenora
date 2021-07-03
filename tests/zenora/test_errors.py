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
            "x-ratelimit-reset-after": 1234.23414,
            "X-RateLimit-Bucket": "abcd1234",
        }
        r.return_value.ok = False
        r.return_value.json.return_value = {
            "errors": {
                "avatar": {
                    "_errors": [{"message": "You are changing avatars too fast"}]
                }
            }
        }
        with pytest.raises(RateLimitException) as e:
            raise_error_or_return(r())
            assert e.message == "You are changing avatars too fast"


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
