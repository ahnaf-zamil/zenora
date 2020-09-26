import typing
import datetime


class Message:

    __slots__ = ["data", "app"]

    def __init__(self, data: typing.Dict, app):
        self.data = data
        self.app = app

    @property
    def id(self):
        return int(self.data["id"])

    @property
    def type(self):
        return int(self.data["type"])

    @property
    def content(self):
        return self.data["content"]

    @property
    def channel(self):
        return self.app.get_channel(int(self.data["channel_id"]))

    @property
    def author(self):
        return self.app.get_user(int(self.data["author"]["id"]))

    @property
    def guild_id(self):
        return int(self.channel.guild_id)

    @property
    def attachments(self):
        return self.data["attachments"]

    @property
    def embeds(self):
        return self.data["embeds"]

    @property
    def mentions(self):
        return [self.app.get_user(i['id']) for i in self.data["mentions"]]

    @property
    def mention_roles(self):
        return self.data["mention_roles"]

    @property
    def pinned(self):
        return self.data["pinned"]

    @property
    def mention_everyone(self):
        return self.data["mention_everyone"]

    @property
    def tts(self):
        return self.data['tts']

    @property
    def timestamp(self):
        return self.data["timestamp"]

    @property
    def edited_timestamp(self):
        return self.data["edited_timestamp"]

    @property
    def flags(self):
        return self.data["flags"]

    def __repr__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("type", self.type),
            ("content", self.content),
            ("channel", self.channel),
            ("guild_id", self.guild_id),
            ("author", self.author),
            ("attachments", self.attachments),
            ("embeds", self.embeds),
            ("mentions", self.mentions),
            ("metion_roles", self.mention_roles),
            ("pinned", self.pinned),
            ("mention_everyone", self.mention_everyone),
            ("tts", self.tts),
            ("timestamp", self.timestamp),
            ("edited_timestamp", self.edited_timestamp),
            ("flags", self.flags)
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )
