import typing


class Emoji:
    __slot__ = ["data", "app"]

    def __init__(self, data: typing.Dict, app):
        self.data = data
        self.app = app

    @property
    def id(self):
        return int(self.data["id"])

    @property
    def name(self):
        return self.data["name"]

    @property
    def roles(self):
        return self.data["roles"]

    @property
    def user(self):
        if "user" in self.data:
            return self.data["user"]
        return None

    @property
    def require_colons(self):
        return self.data["require_colons"]

    @property
    def managed(self):
        return self.data["managed"]

    @property
    def animated(self):
        return self.data["animated"]

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("name", self.name),
            ("roles", self.roles),
            ("user", self.user),
            ("require_colons", self.require_colons),
            ("managed", self.managed),
            ("animated", self.animated),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )
