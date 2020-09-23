import typing
import datetime

from zenora.users import User
from zenora.base.factory import Factory as BaseFactory
from zenora.impl.mapper import ChannelMapper, EmojiMapper


class Factory(BaseFactory):
    def parse_channel(response: typing.Dict, app):
        """Parses response data from Dicord API into channel objects

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        app: zenora.RESTAPI
                Zenora REST API object

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """
        return ChannelMapper.map(response, app)

    def parse_user(response: typing.Dict, app):
        """Parses response data from Dicord API into user objects

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of the user

        Returns
        -------
        zenora.users.User
                Zenora user object
        """
        return User(response, app)

    def parse_emojis(response, app):
        """
        Parse response data from Dicord to Zenora's emoji objects.

        Parameters
        ----------
        response:
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of guild

        Returns
        -------
        :type: [zenora.emojis.Emoji]
                Zenora emoji object

        """
        listOfEmojis = []
        emojis = response
        for emoji in emojis:
            listOfEmojis.append(EmojiMapper.map(emoji, app))

        return listOfEmojis

    def parse_emoji(response, app):
        """
        Parse response data from Dicord into Zenora's emoji object

        Parameters
        ----------
        response:
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of guild

        Returns
        -------
        zenora.emojis.Emoji
                Zenora emoji object

        """
        return EmojiMapper.map(response, app)
