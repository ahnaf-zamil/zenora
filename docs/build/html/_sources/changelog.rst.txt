=========
Changelog
=========

Here you will find the changelogs for most if not every Zenora update since version **0.0.11**.

If you think anything is missing, make a pull request to add it, or contact me on discord.

Version 0.0.34-alpha
====================

- Renamed ``zenora.RESTAPI`` to ``zenora.REST``.

- Added ``zenora.Emoji`` class for emoji support.

- Added IO methods for emoji.

- Added ``zenora.Message`` object.

- Fixed API bugs.

- Released Zenora v0.0.34-alpha.


----

Version 0.0.33-alpha
====================

- Added ``create_dm(id)`` method that returns ``zenora.channels.DMTextChannel`` object.

- ``token_type`` parameter required to instantiate ``zenora.RESTAPI`` object to remove a bug with the ``Bearer`` token type.

- Released Zenora v0.0.33-alpha.


----

Version 0.0.32-alpha
====================

- Added ``modify_current_user()`` method that returns ``zenora.users.User`` object.

- Added ``leave_guild()`` method to leavev servers.

- Added ``get_my_dms()`` that will return a list of ``zenora.channels.DMTextChannel`` objects representing your DM chats.

- Removed ``token_type`` parameter from ``zenora.RESTAPI`` class to remove a bug with the ``Bearer`` token type.

- Released Zenora v0.0.32-alpha.

----


Version 0.0.31-alpha
====================

- Added ``get_current_user()`` method to ``zenora.RESTAPI``

- Renamed ``zenora.users.PartialUser`` to ``zenora.users.User``.

- Added optional properties to ``User`` object that will return ``None`` if API doesn't send response. 

- Released Zenora v0.0.31-alpha.

----

Version 0.0.30-alpha
====================

- Moved response error handlers to ``zenora.utils.helpers``.

- Added a nice welcome message that will be printed on module import.

- Released Zenora v0.0.30-alpha.

----

Version 0.0.29-alpha
====================

- Added ``PartialUser`` object and accessor methods because the API doesn't return all fields as shown in documentation.

- Converted ``zenora.channels.DMTextChannel.recipients`` to list of ``PartialUser`` objects instead of dict.

- Added error raising for ``PartialUser`` object in case of the usage of invalid snowflake ID as argument in accessor method.

- Released Zenora v0.0.29-alpha.

----

Version 0.0.20-alpha
====================

- Updated Documentation.

- Changed ``get_text_channel`` to ``get_channel()`` since it will return any type of channels according to it's ID

- Released Zenora v0.0.20-alpha.

----

Version 0.0.19-alpha
====================

- Added ``GuildVoiceChannel`` & ``DMTextChannel`` models,

- Added accessor methods for the new models.

- Released Zenora v0.0.19-alpha

----

Version 0.0.11-alpha
====================

- Added ``zenora.channels.GuildTextChannel`` model and getter methods.

- Created RESTAPI model for accessing API

- Released Zenora v0.0.11-alpha
