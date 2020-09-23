import abc
import typing
from zenora.channels import GuildTextChannel


class ChannelMapper(abc.ABC):
    @abc.abstractmethod
    def map(response, app) -> typing.Any:
        """Interface of channel mapper

        Maps channel response to object according to channel type.

        Parameters
        ----------
        response: typing.Dict
                API response from Discord

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """


class BaseEmojiMapper(abc.ABC):
    @abc.abstractmethod
    def map(response, app):
        """
        Interface of emoji mapper

        Maps emoji response to object.

        Parameters
        ----------
        response: typing.Dict
                API response from Discord

        Returns
        -------
        zenora.emojis.Emoji
                Zenora emoji object
        """
