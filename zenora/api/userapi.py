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

from zenora.models.connection import Connection
from zenora import Snowflake, SnowflakeOr
from zenora import OwnUser, User
from abc import ABC, abstractmethod

import typing


__all__: typing.Final[typing.List[str]] = ["UserAPI"]


class UserAPI(ABC):
    """A client for using all the user related API functionality"""

    @abstractmethod
    def get_current_user(self) -> OwnUser:
        """Returns the currently logged in user

        Returns:
            OwnUser: An object representing the current user on Discord
        """

    @abstractmethod
    def get_user(self, user_id: typing.Union[str, Snowflake]) -> User:
        """Returns a user with the corresponding ID

        Args:
            user_id (typing.Union[str, Snowflake]): Snowflake ID of the user

        Returns:
            User: An object representing a user on Discord
        """

    @abstractmethod
    def modify_current_user(
        self,
        username: str = None,
        avatar: str = None,
    ) -> OwnUser:
        """Modify the current user's username or avatar

        Args:
            username (str, optional): The user's username. Defaults to None.
            avatar (typing.Literal[".png", ".jpg", ".jpeg", ".gif"], optional): The user's new avatar link. Defaults to None.

        Returns:
            OwnUser: An object representing the current user on Discord
        """

    @abstractmethod
    def get_current_user_connections(self) -> typing.List[Connection]:
        """Returns a list of connection objects for current user

        Returns:
            typing.List[Connection]: List of connection objects
        """

    @abstractmethod
    def create_dm(
        self, user: typing.Union[SnowflakeOr, User]
    ) -> dict:  # Todo: Create DM channel object
        """Creates a DM with a user

        Args:
            user: typing.Union[SnowflakeOr, User]
        Returns:
            dict: DM channel dictionary.
        """
