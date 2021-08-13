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

from zenora.errors import raise_error_or_return

import typing
import requests


__all__: typing.Final[typing.List[str]] = ["Request"]


class Request:
    """Constructs a request to the Discord API"""

    def __init__(
        self,
        token: str,
        url: str,
        method: str,
        *,
        json_data: typing.Optional[dict] = None,
        headers: typing.Optional[dict] = None,
        form_data: typing.Optional[dict] = None,
    ):
        self.token = token
        self.url = url
        self.method = method
        self.json = json_data
        self.headers = headers
        self.form_data = form_data

    def execute(self):
        """Executes the API request"""
        headers = {
            "User-Agent": "{zenora.__name__} {zenora.__version__}",
            "Authorization": f"{self.token}",
        }
        if self.headers:
            headers = self.headers

        if self.json:
            r = requests.request(
                method=self.method,
                url=self.url,
                headers=headers,
                json=self.json,
            )
        else:
            r = requests.request(
                method=self.method,
                url=self.url,
                headers=headers,
                data=self.form_data,
            )

        return raise_error_or_return(r)
