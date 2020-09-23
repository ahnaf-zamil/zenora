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

# DOES NOT WORK IF pip uninstall zenora
# asd asdasd  adasdasd

import zenora
from zenora.impl.mapper import ChannelMapper, EmojiMapper
import unittest


class testChannelMapper(unittest.TestCase):

    # Just trying Travis CI
    def setUp(self):
        """Setting up the data that will be used to check the values from the API mock"""
        self.response = {
            "id": "753859569859690509",
            "last_message_id": "754623102561812511",
            "type": 0,
            "name": "general",
            "position": 4,
            "parent_id": "753859569859690506",
            "topic": None,
            "guild_id": "753859568764977194",
            "permission_overwrites": [],
            "nsfw": False,
            "rate_limit_per_user": 0,
        }
        self.app = {}

    def test_map(self):
        c = ChannelMapper.map(self.response, self.app)
        self.assertTrue(int(c.id) == int(self.response["id"]))


class TestEmojiMapper(unittest.TestCase):
    def setUp(self):
        self.response = {
            "id": "41771983429993937",
            "name": "LUL",
            "roles": ["41771983429993000", "41771983429993111"],
            "user": {
                "username": "Luigi",
                "discriminator": "0002",
                "id": "96008815106887111",
                "avatar": "5500909a3274e1812beb4e8de6631111",
            },
            "require_colons": True,
            "managed": False,
            "animated": False,
        }
        self.app = {}

    def test_map(self):
        e = EmojiMapper.map(self.response, self.app)
        print(e)
        self.assertTrue(int(e.id) == int(self.response["id"]))


if __name__ == "__main__":
    unittest.main()
