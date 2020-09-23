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
import zenora
from zenora.base.rest import RESTAPI as REST
from zenora.impl.factory import Factory as model_factory
from zenora.impl.query import Query


class RESTAPI(REST):

    __slots__ = ["token", "testing"]

    def __init__(
        self, token: str, token_type: str, testing: bool = False
    ) -> None:
        self.token = token
        self.token_type = token_type
        self.testing = testing

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
        if not self.testing:
            response = Query(self.token, self.token_type).channel(snowflake)
        else:
            response = {
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
        return model_factory.parse_channel(response=response, app=self)

    def modify_channel(
        self, snowflake: int, params: typing.Dict
    ) -> typing.Any:
        """Modify Discord Guild Channel

        The snowflake parameter has to be the channel snowflake ID

        Parameters
        ----------
        snowflake : int
                The snowflake ID of the channel.

        args: typing.Dict
                A dictionary containing the changes to the current channel. Check this
                link for all the changes applicable https://discord.com/developers/docs/resources/channel#modify-channel
        """
        response = Query(self.token, self.token_type).modify_channel(
            snowflake, params
        )

        return model_factory.parse_channel(response=response, app=self)

    def delete_channel(self, snowflake: int) -> typing.Any:
        """Delete Discord Guild Channel

        The snowflake parameter has to be the channel snowflake ID

        Parameters
        ----------
        snowflake : int
                The snowflake ID of the channel.
        """
        Query(self.token, self.token_type).delete_channel(snowflake)
        return None

    def get_user(self, snowflake: int) -> typing.Any:
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
        if not self.testing:
            response = Query(self.token, self.token_type).user(snowflake)
        else:
            response = {
                "id": "479287754400989217",
                "username": "Ahnaf",
                "avatar": "9ab336b1e0506f6549d708591991d195",
                "discriminator": "4346",
                "public_flags": 128,
            }
        return model_factory.parse_user(response=response, app=self)

    def get_current_user(self) -> typing.Any:
        """Fetch the current Dicord User


        Returns
        -------
        zenora.users.User
                Zenora user object

        """
        if not self.testing:
            response = Query(self.token, self.token_type).current_user()
        else:
            response = {
                "id": "479287754400989217",
                "username": "Ahnaf",
                "avatar": "9ab336b1e0506f6549d708591991d195",
                "discriminator": "4346",
                "public_flags": 128,
            }
        return model_factory.parse_user(response=response, app=self)

    def get_my_dms(self) -> typing.List:
        """Fetch the current Dicord user's DM channels


        Returns
        -------
        typing.List
                List of Zenora DMTextChannel objects

        """

        if not self.testing:
            response = Query(self.token, self.token_type).current_user_dms()
        else:
            response = [
                {
                    "id": "753798803806748883",
                    "last_message_id": "754896488441708595",
                    "type": 1,
                    "recipients": [
                        {
                            "id": "406882130577063956",
                            "username": "Hjacobs",
                            "avatar": "aa6fb65225a58726292323435512925d",
                            "discriminator": "9441",
                            "public_flags": 0,
                        }
                    ],
                },
                {
                    "id": "736468127210012732",
                    "last_message_id": "736469839983542334",
                    "type": 1,
                    "recipients": [
                        {
                            "id": "503641822141349888",
                            "username": "Someone",
                            "avatar": "a_3df953ed0d85ebc1877762ed9fe29eae",
                            "discriminator": "5555",
                            "public_flags": 128,
                        }
                    ],
                },
            ]
        return [
            model_factory.parse_channel(response=i, app=self) for i in response
        ]

    def modify_current_user(self, args: dict) -> typing.Any:
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
            User(id=753561575532658738, username=Zenora, discriminator=6423, avatar_url=https://cdn.discordapp.com/avatars/753561575532658738/380c68e7a6752e347ed875c2e11a05c4.png?size=1024,
            flags=0, mention=<@753561575532658738>, bot=True, mfa_enabled=True, locale=en-US, verified=True,)


        Returns
        -------
        zenora.users.User
                Zenora user object

        """
        if not self.testing:
            if "avatar" in args:
                args["avatar"] = zenora.File(args["avatar"]).data
            response = Query(self.token, self.token_type).modify_me(args)
        else:
            response = {
                "id": "479287754400989217",
                "username": "Ahnaf",
                "avatar": "9ab336b1e0506f6549d708591991d195",
                "discriminator": "4346",
                "public_flags": 128,
            }
        return model_factory.parse_user(response=response, app=self)

    def create_dm(self, recipient_id: int) -> zenora.channels.DMTextChannel:
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
        if not self.testing:
            response = Query(self.token, self.token_type).create_dm(
                recipient_id
            )
        else:
            response = {
                "id": "753798803806748883",
                "last_message_id": "754896488441708595",
                "type": 1,
                "recipients": [
                    {
                        "id": "406882130577063956",
                        "username": "Hjacobs",
                        "avatar": "aa6fb65225a58726292323435512925d",
                        "discriminator": "9441",
                        "public_flags": 0,
                    }
                ],
            }
        return model_factory.parse_channel(response=response, app=self)

    def leave_guild(self, snowflake: int) -> typing.Optional[None]:
        """Leave a Discord server (current user)

        Parameters
        ----------

        snowflake: int
                The ID of the Discord Server

        Returns
        -------
        code: int
            Code for response status. Will return 204 on success

        """
        if not self.testing:
            response = Query(self.token, self.token_type).leave_guild(
                snowflake
            )
        else:
            response = 204
        return response

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
        if not self.testing:
            response = Query(self.token, self.token_type).get_emojis(snowflake)
        else:
            response = [
                {
                    "name": "test_emoji",
                    "roles": [],
                    "id": "758255225319981076",
                    "require_colons": True,
                    "managed": False,
                    "animated": False,
                    "available": True,
                    "user": {
                        "id": "592703489386348544",
                        "username": "db",
                        "avatar": "e07296d96c4f6c75b4fbbf25ec7d28b6",
                        "discriminator": "3272",
                        "public_flags": 0,
                    },
                },
                {
                    "name": "test_emoji2",
                    "roles": [],
                    "id": "758255421768335370",
                    "require_colons": True,
                    "managed": False,
                    "animated": False,
                    "available": True,
                    "user": {
                        "id": "592703489386348544",
                        "username": "db",
                        "avatar": "e07296d96c4f6c75b4fbbf25ec7d28b6",
                        "discriminator": "3272",
                        "public_flags": 0,
                    },
                },
            ]
        return model_factory.parse_emojis(response=response, app=self)

    def get_emoji(self, snowflake, emoji_id):
        """Get emoji for guild by emoji_id

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
        if not self.testing:
            response = Query(self.token, self.token_type).get_emoji(
                snowflake, emoji_id
            )
        else:
            response = {
                "name": "test_emoji",
                "roles": [],
                "id": "758255225319981076",
                "require_colons": True,
                "managed": False,
                "animated": False,
                "available": True,
                "user": {
                    "id": "592703489386348544",
                    "username": "db",
                    "avatar": "e07296d96c4f6c75b4fbbf25ec7d28b6",
                    "discriminator": "3272",
                    "public_flags": 0,
                },
            }
        return model_factory.parse_emoji(response=response, app=self)

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
        if not self.testing:
            response = Query(self.token, self.token_type).post_emoji(
                snowflake, name, image_url, roles
            )
        else:
            # Create new emoji object
            response = {
                "name": "test_emoji",
                "roles": [],
                "id": "758255225319981076",
                "require_colons": True,
                "managed": False,
                "animated": False,
                "available": True,
                "user": {
                    "id": "592703489386348544",
                    "username": "db",
                    "avatar": "e07296d96c4f6c75b4fbbf25ec7d28b6",
                    "discriminator": "3272",
                    "public_flags": 0,
                },
            }
        return model_factory.parse_emoji(response=response, app=self)

    def patch_emoji(self, snowflake, emoji_id, name, roles):
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
        if not self.testing:
            response = Query(self.token, self.token_type).patch_emoji(
                snowflake, emoji_id, name, roles
            )
        else:
            # Updated emoji name `test_emoji` to `new_test_emoji` for testing
            response = {
                "name": "new_test_emoji",
                "roles": [],
                "id": "758255225319981076",
                "require_colons": True,
                "managed": False,
                "animated": False,
                "available": True,
                "user": {
                    "id": "592703489386348544",
                    "username": "db",
                    "avatar": "e07296d96c4f6c75b4fbbf25ec7d28b6",
                    "discriminator": "3272",
                    "public_flags": 0,
                },
            }
        return model_factory.parse_emoji(response=response, app=self)

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
        if not self.testing:
            response = Query(self.token, self.token_type).delete_emoji(
                snowflake,
                emoji_id,
            )
        else:
            response = 204
        return response
