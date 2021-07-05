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

from zenora.models.connection import Connection
from zenora.models.user import User
from datetime import datetime

import zenora


def test_snowflake():
    snowflake_int = 479287754400989217
    snowflake = zenora.Snowflake(snowflake_int)

    assert snowflake.internal_worker_id == (snowflake_int & 0x3E0000) >> 17
    assert snowflake.internal_process_id == (snowflake_int & 0x1F000) >> 12
    assert snowflake.increment == snowflake_int & 0xFFF
    assert (
        snowflake.timestamp
        == datetime.fromtimestamp(
            ((snowflake_int >> 22) + 1420070400000) / 1000
        ).astimezone()
    )


def test_user():
    user_payload = {
        "id": 479287754400989217,
        "username": "Ahnaf",
        "discriminator": "4346",
        "avatar": "abcdefg",
        "bio": "I am pog",
    }

    user = User(**user_payload)

    assert (
        user.avatar_url
        == f"https://cdn.discordapp.com/avatars/{user_payload['id']}/{user_payload['avatar']}.png"
    )
    assert user.is_bot is None
    assert user.bio == "I am pog"
    assert user.avatar_hash == user_payload["avatar"]


def test_connection():
    connection_payload = {
        "id": "12345",
        "name": "DevGuyAhnaf",
        "type": "YouTube",
        "visibility": 0,
        "integrations": [],
    }

    connection = Connection(**connection_payload)

    assert connection.id == connection_payload["id"]
    assert connection.name == connection_payload["name"]
    assert connection.type == connection_payload["type"]
    assert connection.visibility == connection_payload["visibility"]
