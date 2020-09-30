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

import abc
import typing


class Query(abc.ABC):
    __slots__ = ["token", "token_type"]

    def __init__(self, token: str, token_type: str):
        self.token = token
        self.token_type = token_type

    @abc.abstractmethod
    def channel(self, snonwflake: int) -> typing.Dict:
        """Interface for the REST API query to get channels.

        Parameters:
        snowflake: int
                The channel ID of a Discord channel

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def user(self, snowflake: int) -> typing.Dict:
        """Interface for the REST API query to get user.

        Parameters:
        snowflake: int
                The ID of a Discord User

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def message(self, channel_id, msg_id) -> typing.Dict:
        """Interface for the REST API query to get message according to ID.
        Parameters:
        channel_id: int
                The snowflake ID of a Discord channel
        msg_id: int
                The snowflake ID of a Discord message.
        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def current_user(self) -> typing.Dict:
        """Interface for the REST API query to get current user.

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def modify_me(self, args: dict) -> typing.Dict:
        """Interface for the REST API query to modify current user.

        Returns:
        typing.Dict:
                A dictionary object that will be used to parse the data
                into objects
        """

    @abc.abstractmethod
    def modify_channel(self, channel_id: int, args: typing.Dict):
        """Interface for the REST API query to modify guild channel.

        Returns:
        channel_id: int
                The snowflake ID of the channel.
        typing.Dict:
                A dictionary object that will be used to parse the data
                into objects

        """

    @abc.abstractmethod
    def delete_channel(self, channel_id):
        """Interface for the REST API query to delete guild channel.

        Returns:
        channel_id: int
                The snowflake ID of the channel.

        """

    @abc.abstractmethod
    def leave_guild(self, snowflake: int):
        """Interface for the REST API query to leave a guild.

        Returns:
        code: int
            Code for response status. Will return 204 on success
        """

    @abc.abstractmethod
    def current_user_dms(self) -> typing.Dict:
        """Interface for the REST API query to fetch current user's DMs list

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def create_dm(self, recipient_id: int) -> typing.Dict:
        """Interface for the REST API query to create a DM with a specific user according to ID

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def get_emojis(self, snowflake):
        """
        Interface for the REST API query to get emojis for guild

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def get_emoji(self, snowflake, emoji_id):
        """
        Interface for the RESt API query to get emoji for guild and emoji_id

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def create_emoji(self, snowflake, name, image_url, roles):
        """
        Inerface for the REST API query to add new emoji to a guild

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def update_emoji(self, snowflake, name, roles):
        """
        Interface for the rest API query to update emoji for guild

        Returns:
        Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def delete_emoji(self, snowflake, emoji_id):
        """
        Interface for the rest API query to delete emoji for guild

        Returns:
        code: int
            Code for response status. Will return 204 on success
        """
