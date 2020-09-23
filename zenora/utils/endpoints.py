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


"""Endpoints for the Discord REST API"""

BASE_URL = "https://discord.com/api/v6"
CDN_URL = "https://cdn.discordapp.com"

# Channels
FETCH_CHANNEL = "/channels/{}"
DMS_LIST = "/users/@me/channels"

# Users
FETCH_USER = "/users/{}"
FETCH_CURRENT_USER = "/users/@me"

# Guilds
GET_GUILD = "/guilds/{}"

# Emojis
EMOJI = "/emojis"
EMOJI_ID = "/emojis/{}"

"""CDN Endpoints"""

AVATAR_URL = "/avatars/{}/{}.png?size=1024"
DEFAULT_AVATAR_URL = (
    "https://discordapp.com/assets/322c936a8c8be1b803cd94861bdfa868.png"
)
