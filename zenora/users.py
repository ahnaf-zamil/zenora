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
from .utils.endpoints import DEFAULT_AVATAR_URL, CDN_URL, AVATAR_URL


class User:
    """A user object for API response.

    :return: Zenora user object
    :rtype: zenora.users.User
    """

    __slots__ = ["data", "app"]

    def __init__(self, data, app) -> None:
        self.data = data
        self.app = app

    @property
    def id(self) -> typing.Optional[int]:
        """Returns The snowflake ID of the user."""
        return int(self.data["id"])

    @property
    def username(self) -> typing.Optional[str]:
        """Returns the username of the user."""
        return self.data["username"]

    @property
    def discriminator(self) -> typing.Optional[int]:
        """Returns the user's discriminator."""
        return self.data["discriminator"]

    @property
    def avatar_url(self) -> typing.Optional[str]:
        """Returns the user's avatar url"""
        if self.data["avatar"] is not None:
            return CDN_URL + AVATAR_URL.format(self.id, self.data["avatar"])
        return DEFAULT_AVATAR_URL

    @property
    def flags(self) -> typing.Optional[int]:
        """Returns the user's public flags """
        return self.data["public_flags"]

    @property
    def mention(self) -> typing.Optional[str]:
        """Returns the user's mention"""
        return f"<@{self.id}>"

    @property
    def bot(self) -> typing.Optional[bool]:
        """Returns the user's mention (optional)"""
        return self.data["bot"] if "bot" in self.data else None

    @property
    def is_system(self) -> typing.Optional[bool]:
        """Returns if the user is a Discord System user or not (optional)"""
        return self.data["system"] if "system" in self.data else None

    @property
    def mfa_enabled(self) -> typing.Optional[bool]:
        """Returns whether the user has two factor enabled on their account (optional)"""
        return self.data["mfa_enabled"] if "mfa_enabled" in self.data else None

    @property
    def locale(self) -> typing.Optional[str]:
        """Returns the user's chosen language option (optional)"""
        return self.data["locale"] if "locale" in self.data else None

    @property
    def verified(self) -> typing.Optional[bool]:
        """Returns whether the email on this account has been verified (optional)"""
        return self.data["verified"] if "verified" in self.data else None

    @property
    def email(self) -> typing.Optional[str]:
        """Returns the user's email (optional)"""
        return self.data["email"] if "email" in self.data else None

    @property
    def premium_type(self) -> typing.Optional[int]:
        """Returns the type of Nitro subscription on a user's account (optional)"""
        return (
            [None, "Nitro Classic", "Nitro"][self.data["premium_type"]]
            if "premium_type" in self.data
            else None
        )

    def __repr__(self) -> typing.Optional[str]:
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("username", self.username),
            ("discriminator", self.discriminator),
            ("avatar_url", self.avatar_url),
            ("flags", self.flags),
            ("mention", self.mention),
            ("bot", self.bot),
            ("is_system", self.is_system),
            ("mfa_enabled", self.mfa_enabled),
            ("locale", self.locale),
            ("verified", self.verified),
            ("email", self.email),
            ("premium_type", self.premium_type),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join(f"{i[0]}={i[1]}," for i in attrs if i[1] is not None),
        )
