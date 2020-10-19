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
from dataclasses import dataclass
from .utils.endpoints import DEFAULT_AVATAR_URL, CDN_URL, AVATAR_URL

@dataclass
class User:
    """A user object for API response.

    :return: Zenora user object
    :rtype: zenora.users.User
    """


    app: typing.Any
    id: int
    username: str
    discriminator: int
    avatar: typing.Optional[str] = None
    bot: typing.Optional[bool] = None
    system: typing.Optional[bool] = None
    mfa_enabled: typing.Optional[bool] = None
    locale: typing.Optional[str] = None
    verified: typing.Optional[bool] = None
    email: typing.Optional[str] = None
    public_flags: typing.Optional[int] = None
    flags: typing.Optional[int] = None


    @property
    def avatar_url(self) -> str:
        """Returns the user's avatar url"""
        if self.avatar is not None:
            return CDN_URL + AVATAR_URL.format(self.id, self.avatar)
        return DEFAULT_AVATAR_URL
    
    @property
    def mention(self) -> typing.Optional[str]:
        """Returns the user's mention"""
        return f"<@{self.id}>"

    
    def __str__(self) -> typing.Optional[str]:
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("username", self.username),
            ("discriminator", self.discriminator),
            ("avatar_url", self.avatar_url),
            ("public_flags", self.public_flags),
            ("mention", self.mention),
            ("bot", self.bot),
            ("system", self.system),
            ("mfa_enabled", self.mfa_enabled),
            ("locale", self.locale),
            ("verified", self.verified),
            ("email", self.email)
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join(f"{i[0]}={i[1]}," for i in attrs if i[1] is not None),
        )