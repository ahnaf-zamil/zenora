# Copyright (c) 2021 K.M Ahnaf Zamil

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
from zenora.utils import convert_image_to_data, is_valid_url
import zenora
import pytest


class MockObj:
    __str__ = zenora.utils.get__str__

    test = "public attribute"
    _test = "private attribute"

    def callable_function(self):
        return


def test_get__str__():
    obj = MockObj()
    assert str(obj) == 'MockObj(test="public attribute")'


def test_is_valid_url():
    valid_urls = [
        "https://google.com",
        "http://localhost",
        "https://website.com/img.png",
        "https://ahnafzamil.com",
    ]

    for x in valid_urls:
        assert is_valid_url(x)

    invalid_urls = [
        "localhost",
        "google.com",
        "https://github,com",
        "htts://ahnafzamil.com",
        "hptp://discord.com",
    ]

    for x in invalid_urls:
        assert not is_valid_url(x)


def test_convert_image_to_data():
    # With query string
    url = "https://cdn.discordapp.com/avatars/822836943619620895/889efab13583e8f7561b456aaa020dec.png?size=32"
    assert "data:image/png;base64," in convert_image_to_data(url)

    # Without query string
    url = "https://cdn.discordapp.com/avatars/822836943619620895/889efab13583e8f7561b456aaa020dec.png"
    assert "data:image/png;base64," in convert_image_to_data(url)

    # For jpg and jpeg
    url = "https://cdn.discordapp.com/avatars/822836943619620895/889efab13583e8f7561b456aaa020dec.jpg"
    assert "data:image/jpeg;base64," in convert_image_to_data(url)

    url = "https://cdn.discordapp.com/avatars/822836943619620895/889efab13583e8f7561b456aaa020dec.jpeg"
    assert "data:image/jpeg;base64," in convert_image_to_data(url)

    # For invalid mimetypes
    with pytest.raises(BadURLException):
        convert_image_to_data("https://website.com/file.exe")

    with pytest.raises(BadURLException):
        convert_image_to_data("https://website.com/file")
