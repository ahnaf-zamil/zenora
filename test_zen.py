import zenora
import testconfig

api = zenora.REST(token=testconfig.token, token_type="Bot")

# channel = api.get_channel(testconfig.channel_id)
# print(channel)
# print(channel.delete())

print("\n\n>>> Add new emoji")


updated = api.get_guild_emoji(guild_id=753859568764977194)

print(updated)
