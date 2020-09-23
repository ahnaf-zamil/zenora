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
import abc
from ..channels import DMTextChannel, GuildTextChannel, GuildVoiceChannel
from ..users import User


class RESTAPI(abc.ABC):
    """Base interface for the implementation of the REST API."""

    __slots__ = ["token", "token_type", "testing"]

    def __init__(
        self, token: str, token_type: str, testing: bool = False
    ) -> None:
        self.token = token
        self.token_type = token_type
        self.testing = testing

    @abc.abstractmethod
    def get_channel(self, snowflake: int) -> typing.Any:
        """Fetch Dicord Channel

        This has to be the channel snowflake ID


        Parameters
        ----------

        snowflake: int
                The channel ID of the specific channel you want to fetch

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """

    @abc.abstractmethod
    def modify_channel(
        self, snowflake: int, params: typing.Dict
    ) -> typing.Any:
        """Modify Discord Guild Channel

        The snowflake parameter has to be the channel snowflake ID


        Parameters
        ----------

        snowflake: int
                The channel ID of the specific channel you want to fetch


        Parameters
        ----------
        snowflake : int
                The snowflake ID of the channel.

        args: typing.Dict
                A dictionary containing the changes to the current channel. Check this
                link for all the changes applicable https://discord.com/developers/docs/resources/channel#modify-channel
        """

    @abc.abstractmethod
    def delete_channel(self, snowflake: int) -> typing.Any:
        """Delete Discord Guild Channel

        The snowflake parameter has to be the channel snowflake ID

        Parameters
        ----------
        snowflake : int
                The snowflake ID of the channel.
        """

    @abc.abstractmethod
    def get_user(self, snowflake: int) -> typing.Optional[User]:
        """Fetch Dicord User

        This has to be the user's snowflake ID


        Parameters
        ----------

        snowflake: int
                The ID of the Discord User

        Returns
        -------
        zenora.users.User
                Zenora user object

        """

    @abc.abstractmethod
    def get_my_dms(self) -> typing.List[DMTextChannel]:
        """Fetch the current Dicord user's DM channels


        Returns
        -------
        typing.List
                List of Zenora DMTextChannel objects

        """

    @abc.abstractmethod
    def modify_current_user(self, args: dict) -> typing.Optional[User]:
        """Modify current discord User


        Parameters
        ----------
        args: typing.Dict
                A dictionary containing the changes to the current user. This has to be either
                their username, avatar or both

        Example
        -------
        .. code-block:: python


            >>> some_api_instance.modify_current_user({'username' : 'FroggyMan', 'avatar' : 'https://cdn.discordapp.com/avatars/753561575532658738/0cf89f88a3ba4e226c6f1c72a9242dd8.png'})
            User(id=753561575532658738, username=FroggyMan, discriminator=6423, avatar_url=https://cdn.discordapp.com/avatars/753561575532658738/380c68e7a6752e347ed875c2e11a05c4.png?size=1024,
            flags=0, mention=<@753561575532658738>, bot=True, mfa_enabled=True, locale=en-US, verified=True,)



        Returns
        -------
        zenora.users.User
                Zenora user object

        """

    @abc.abstractmethod
    def create_dm(self, recipient_id: int) -> typing.Optional[DMTextChannel]:
        """Creates DM text channel with a specified user according to snowflake ID

        Parameters
        ----------
        recipient_id: int
                The snowflake ID of the user with whom the DM would be opened

        Returns
        -------
        zenora.channels.DMTextChannel
                Zenora DM Text channel object

        """

    @abc.abstractmethod
    def leave_guild(self, snowflake: int) -> typing.Optional[None]:
        """Leave a Discord server (current user)

        Parameters
        ----------

        snowflake: int
                The ID of the Discord Server

        Returns
        -------
        None

        """

    @abc.abstractmethod
    def get_emojis(self, snowflake):
        """
        Get list of all emojis for guild

        Parameters
        ----------

        snowflake: int
                The id of the guild

        Returns
        ------
        :type [zenora.emojis.Emoji]
                List of emoji's
        """

    @abc.abstractmethod
    def get_emoji(self, snowflake, emoji_id):
        """
        Get emoji for guild by emoji_id


        Parameters
        ----------
        snowflake: int
            The id of the guild
        emoji_id: int
            The id of emoji

        Returns
        -------
        zenora.emojis.Emoji
            Zenora emoji object

        """

    @abc.abstractmethod
    def post_emoji(self, snowflake, name, image_url, roles):
        """
        Add new emoji for guild


        Parameters
        ----------
        snowflake: int
            The id of the guild
        name: str
            Name of the emoji
        image_url: str
            Address of image that used for emoji
        roles: [int]
            Array of snowflakes

        Returns
        -------
        zenora.emojis.Emoji
            Zenora emoji object
        """

    @abc.abstractmethod
    def patch_emoji(self, snowflake, name, roles):
        """
        Update emoji for guild


        Parameters
        ----------
        snowflake: int
            The id of the guild
        name: str
            Name of the emoji
        roles: [int]
            Array of snowflake

        Returns
        -------
        zenora.emojis.Emoji
            Zenora emoji object
        """

    @abc.abstractmethod
    def delete_emoji(self, snowflake, emoji_id):
        """
        Delete emoji for guild


        Parameters
        ----------
        snowflake: int
            The id of the guild
        emoji_id: int
            The id of emoji

        Returns
        -------
        zenora.emojis.Emoji
            Zenora emoji object
        """
