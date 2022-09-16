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

from zenora.exceptions import (
    APIError,
    AuthenticationError,
    CloudflareException,
    RateLimitException,
)
from zenora.routes import BASE_URL
from typing import Optional, Dict, Any, NoReturn

import json
import requests

_401_msg = {"invalid_client": "Invalid Client Secret has been passed"}


def _handle_401(data: dict) -> None:
    if data.get("message"):
        raise AuthenticationError(data["message"])
    else:
        msg = _401_msg.get(data["error"])
        raise AuthenticationError(
            msg if msg else f"Unknown 401 exception `{data['error']}`"
        )


def _handle_other_err(data: dict) -> None:
    if "error" in data:
        raise APIError(f"{data['error_description']}")
    for x in data["errors"]:
        err = data["errors"][x]
        if "_errors" in err:
            msg = err["_errors"][0]["message"]
        else:
            msg = data["message"]
        raise APIError(f"Code {data['code']}. Message: {msg}")


def raise_error_or_return(
    r: requests.Response,
) -> Optional[Dict[str, Any]]:
    try:
        json_data = r.json()
    except json.decoder.JSONDecodeError:
        raise CloudflareException("Cloudflare blocking API request to Discord")

    if not r.ok:
        if "X-RateLimit-Bucket" in r.headers:  # Rate limited
            return _handle_rate_limit(r)
        elif r.status_code == 401:  # Unauthorized
            _handle_401(json_data)
        else:
            _handle_other_err(json_data)
        return None  # Just so that MyPy doesn't yell at me
    else:
        return json_data


def _handle_rate_limit(r: requests.Response) -> NoReturn:
    headers = r.headers

    if headers.get("X-RateLimit-Global"):
        raise RateLimitException(
            f"Being rate limited globally, will reset after {headers['X-RateLimit-Reset-After']}s.",
            r.headers,
        )

    raise RateLimitException(
        "Being rate limited on {}, will reset after {}s. Bucket: {}".format(
            r.url.replace(BASE_URL, ""),
            headers["X-RateLimit-Reset-After"],
            r.headers["X-RateLimit-Bucket"],
        ),
        r.headers,
    )
