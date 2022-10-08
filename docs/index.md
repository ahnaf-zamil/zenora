![](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=flat-square)
![](https://img.shields.io/badge/Code%20Style-Black-black?style=flat-square)
![](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue?style=flat-square)
![](https://gitlab.com/ahnaf-zamil/zenora/badges/master/pipeline.svg)]
![](https://img.shields.io/pypi/v/zenora.svg?style=flat-square)

# Introduction

Zenora is a synchronous library for accessing the Discord REST API.

It allows you to access the API without async/await. And also gives you REST-only API access, not the gateway.
Pretty useful for making bot web dashboards, or desktop applications, etc. Oauth and other features will be added soon.

This library is currently unfinished but you can help speed up the development by contributing and submitting pull requests to the repository.
It is working in its current state but I'd love to see more functionality added further down the line!

Repository: [`View on GitHub`](https://github.com/ahnaf-zamil/zenora)

If you need any help with this library at any point feel free to DM me on Discord (Ahnaf#4346).

If you think you have found a bug or other problem with the library, or you would like to suggest a feature,
you should submit an issue on the GitHub repository [here](https://github.com/ahnaf-zamil/zenora/issues).
Before doing so you should make sure you are on the latest version of the library and check to see if an issue
already exists for your bug or feature. You can also join the owner's [Discord server](https://discord.gg/3chuca3EMh).

**Contributors:**

-   [Ahnaf#4346 (creator)](https://github.com/ahnaf-zamil/)

# Getting Started

Zenora can be installed be Python's package manager, pip:

`pip install git+https://github.com/ahnaf-zamil/zenora` (from GitHub)

or

`pip install zenora` (from PyPi)

> Note: This library is dependent on [Requests](https://pypi.org/project/requests/).

**Usage**

```py
from zenora import APIClient

client = APIClient(token="...")
# There is also a set_token method which can be used to replace the token later on

# Make API request to get the currently logged in user object
user = client.users.get_current_user()

# Use the data :D
print(user.username)
```

# Using Oauth

Zenora can be used for accessing the Discord Oauth API. It is very simple to use, and reduces a lot
of the hassle for implementing Discord Oauth in your application. But before you do try out Zenora, you need to
know how to use get the authorization code from the Discord API in order to use it (this is mandatory and cannot be
avoided as Zenora depends on that code in order to get the access token).

Link: https://discord.com/developers/docs/topics/oauth2#authorization-code-grant

Once you have the authorization code, Zenora will do the rest of the work for you. Just call some functions and you will get your
access token and will be able to use that to with the Discord API.

**Usage**

```py

from zenora import APIClient

TOKEN = "Your bot's token"
client = APIClient(
    TOKEN,
    client_secret="Your bot's client secret",
)

oauth_url = "your oauth redirect uri"

...

code = "the authorization code that you get from the Discord API everytime someone uses your Oauth application"

access_token = client.oauth.get_access_token(
    code, redirect_uri=oauth_url
).access_token


# Setting it to bearer because we are using Oauth here
bearer_client = APIClient(access_token, bearer=True)

# Query the user's joined guilds
guilds = bearer_client.users.get_my_guilds()

print(guilds) # Prints it out :)
```

If you want to know how to use Oauth with a specific web framework, check out the [Examples section](https://github.com/ahnaf-zamil/zenora/tree/master/examples) of the repository.
