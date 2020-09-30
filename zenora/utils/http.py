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
import requests
from requests import Session
from zenora.errors import MissingAccess, AvatarError, InvalidSnowflake

# Request functions


def fetch(
    url: str,
    headers: typing.Dict[str, str],
    params: typing.Dict[str, str] = {},
) -> typing.Dict:
    r = requests.get(url=url, headers=headers, params=params)
    r.raise_for_status()
    return r.json()


def post(
    url: str,
    headers: typing.Dict[str, str],
    params: typing.Dict[str, str] = {},
) -> typing.Dict:

    r = requests.post(url=url, headers=headers, json=params)
    r.raise_for_status()
    return r.json()


def patch(
    url: str,
    headers: typing.Dict[str, str],
    params: typing.Dict[str, str] = {},
) -> typing.Dict:
    r = requests.patch(url=url, headers=headers, json=params)
    r.raise_for_status()
    return r.json()


def delete(
    url: str,
    headers: typing.Dict[str, str],
    params: typing.Dict[str, str] = {},
) -> typing.Dict:
    r = requests.delete(url=url, headers=headers, json=params)
    r.raise_for_status()
    return r


# Utility functions


def error_checker(data: typing.Dict) -> None:
    if data.get("user_id") or data.get("channel_id"):
        raise InvalidSnowflake(
            data.get("user_id")[0]
            if data.get("user_id") is not None
            else data.get("channel_id")[0]
        )
    elif data.get("code"):
        if data.get("code") == 50001:
            raise MissingAccess(data.get("message"))
        else:
            raise InvalidSnowflake(data.get("message"))
    elif data.get("avatar"):
        if isinstance(data.get("avatar"), list):
            raise AvatarError(data.get("avatar")[0])


def get_file(url):
    # Downloading Image from link
    r = requests.get(url=url, stream=True)
    return r
