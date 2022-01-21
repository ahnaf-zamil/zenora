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

from zenora.deserializers import deserialize_model
from zenora import OwnUser

import pytest


def test_deserialize_model():
    data = {"id": 12345, "username": "poggere", "discriminator": 1234}

    user = deserialize_model(OwnUser, data)

    assert type(user) == OwnUser
    assert user.id == data["id"]

    data = {
        "id": 12345,
        "username": "poggere",
        "discriminator": 1234,
        "blah_blah": "blah",
    }

    user = deserialize_model(
        OwnUser, data
    )  # Should not include the blah_blah in the object
    assert type(user) == OwnUser
    assert not hasattr(user, "blah_blah")

    with pytest.raises(AttributeError):
        user.blah_blah
