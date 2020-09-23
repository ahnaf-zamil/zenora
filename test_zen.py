import zenora
import testconfig

api = zenora.RESTAPI(token=testconfig.token, token_type="Bot")

# channel = api.get_channel(testconfig.channel_id)
# print(channel)
# print(channel.delete())

print("\n\n>>> Add new emoji")
new_emoji = api.post_emoji(
    testconfig.guild_id,
    "demo_emoji",
    testconfig.emoji["image_url"],
    testconfig.emoji["roles"],
)
print(new_emoji)

print("\n\n>>> Get all emojis\n\n")
emojis = api.get_emojis(testconfig.guild_id)
for emoji in emojis:
    print(emoji)

print("\n\n>>> Get a emoji")
emoji = api.get_emoji(testconfig.guild_id, new_emoji.id)
print(emoji)


print("\n\n>>> Update emoji")
emoji = api.patch_emoji(
    testconfig.guild_id,
    new_emoji.id,
    "demo_emoji_2",
    testconfig.emoji["roles"],
)
print(emoji)

print("\n\n>>> Delete emoji")
response_code = api.delete_emoji(testconfig.guild_id, new_emoji.id)
print(response_code)
