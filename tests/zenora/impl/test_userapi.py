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
from zenora.routes import CDN_URL, USER_AVATAR
from zenora.models.snowflake import Snowflake
from zenora.models.user import OwnUser, User
from unittest import mock

import pytest
import requests
import zenora


@pytest.fixture()
def api():
    with mock.patch.object(zenora.UserAPIImpl, "get_current_user"):
        return zenora.APIClient("this token is so pog").users


def test_get_current_user(api: zenora.UserAPI):
    with mock.patch.object(requests, "request") as r:
        current_user = {
            "id": "479287754400989217",
            "username": "Ahnaf",
            "discriminator": "4346",
            "verified": True,
        }

        r.return_value.status_code = 200
        r.return_value.json.return_value = current_user
        user = api.get_current_user()
        r.assert_called_once()

        assert type(user) == OwnUser
        assert user.id == current_user["id"]
        assert user.username == current_user["username"]
        assert user.discriminator == current_user["discriminator"]
        assert user.is_verified == current_user["verified"]


def test_get_user(api: zenora.UserAPI):
    with mock.patch.object(requests, "request") as r:
        testing_user = {
            "id": "514858928983506959",
            "username": "shab",
            "discriminator": "1753",
            "avatar": "testingtesting",
        }

        r.return_value.status_code = 200
        r.return_value.json.return_value = testing_user
        user = api.get_user(testing_user["id"])
        r.assert_called_once()

        assert type(user) == User
        assert user.id == testing_user["id"]
        assert user.username == testing_user["username"]
        assert user.discriminator == testing_user["discriminator"]
        assert (
            user.avatar_url_as(format=".png", size=1024)
            == f"{CDN_URL}{USER_AVATAR}/{testing_user['id']}/{testing_user['avatar']}.png?size=1024"
        )
        assert user.get_snowflake_id() == Snowflake(testing_user["id"])


def test_modify_current_user(api: zenora.UserAPI):
    with mock.patch.object(requests, "request") as r:
        old_user = OwnUser(
            **{
                "id": "714468017542791228",
                "username": "DevHyperCoder",
                "discriminator": "1498",
                "avatar": "testingtesting",
            }
        )

        new_user_payload = r.return_value.json.return_value = {
            "id": "714468017542791228",
            "username": "The Normal One",
            "discriminator": "1498",
            "avatar": "04a3b7319ce6c53bf24e9ea79e2727c4",
        }

        r.return_value.status_code = 200

        new_user = api.modify_current_user(
            username=new_user_payload["username"],
            avatar=f"https://cdn.discordapp.com/avatars/479287754400989217/{new_user_payload['avatar']}.png",
        )

        r.assert_called_once()

        assert old_user.username != new_user.username
        assert old_user.avatar_hash != new_user.avatar_hash
        assert new_user.username == new_user_payload["username"]


def test_get_current_user_connections(api: zenora.UserAPI):
    with mock.patch.object(requests, "request") as r:
        connections = api.get_current_user_connections()
        for x in connections:
            assert type(x) == type(Connection)