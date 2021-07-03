from zenora.exceptions import APIError, CloudflareException, RateLimitException

import json
import typing
import requests


def raise_error_or_return(r: requests.Response) -> typing.Optional[dict]:
    try:
        json_data = r.json()
    except json.decoder.JSONDecodeError:
        raise CloudflareException("Cloudflare blocking API request to Discord")

    if not r.ok:
        if "X-RateLimit-Bucket" in r.headers:
            handle_rate_limit(r)
        else:
            for x in json_data["errors"]:
                if "_errors" in json_data["errors"][x]:
                    msg = json_data["errors"][x]["_errors"][0]["message"]
                else:
                    msg = json_data["errors"][x][0]["message"]
                raise APIError(f"API error {json_data['code']}. Message: {msg}")
    else:
        return json_data


def handle_rate_limit(r: requests.Response):
    json_data = r.json()
    for x in json_data["errors"]:
        raise RateLimitException(
            f"Being rate limited, will reset after {r.headers['x-ratelimit-reset-after']}s."
            + f" Message: {json_data['errors'][x]['_errors'][0]['message']}",
            r.headers,
        )
