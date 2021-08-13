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

from zenora.exceptions import BadURLException

import re
import base64
import mimetypes
import typing
import requests

__all__: typing.Final[typing.List[str]] = [
    "get__str__",
    "is_valid_url",
    "convert_image_to_data",
]

regex = re.compile(
    r"^(?:http)s?://"
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
    r"localhost|"
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    r"(?::\d+)?"
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


def get__str__(obj) -> str:
    attributes = ", ".join(
        [
            f'{atr}="{getattr(obj, atr)}"'
            for atr in dir(obj)
            if not atr.startswith("_") and not callable(getattr(obj, atr))
        ]
    )
    return f"{obj.__class__.__name__}({attributes})"


def is_valid_url(url) -> bool:
    return re.match(regex, url) is not None


def convert_image_to_data(path: str):
    if "?" in path:
        path = path.split("?")[0]
    mime, _ = mimetypes.guess_type(path)
    if mime not in ["image/jpeg", "image/png", "image/gif"]:
        raise BadURLException(
            "Invalid file type. File must be jpeg/jpg, png, or gif"
        )

    if is_valid_url(path):
        data = requests.get(path, timeout=5).content
        encoded_body = base64.b64encode(data)
        return "data:%s;base64,%s" % (mime, encoded_body.decode())
    else:
        raise BadURLException(f"Invalid URL: {path}")


def extract_snowflake_from_object(obj: typing.Any):
    if isinstance(obj, int):
        return str(obj)
    else:
        return str(int(obj.id))
