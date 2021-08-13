# Zenora

[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![prs](https://img.shields.io/github/issues-pr/ahnaf-zamil/zenora?color=red&style=flat-square)](https://github.com/ahnaf-zamil/zenora/pulls)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-black?style=flat-square)](https://github.com/psf/black)
[![pyvers](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue?style=flat-square)](https://pypi.org/project/zenora)
[![Build](https://img.shields.io/github/workflow/status/ahnaf-zamil/zenora/Python%20package?logo=GitHub&style=flat-square&label=Build)](https://github.com/ahnaf-zamil/zenora/actions/workflows/python-package.yml)<br/>
[![Pypi](https://img.shields.io/pypi/v/zenora.svg?style=flat-square)](https://pypi.org/project/zenora/)
[![Docs](https://img.shields.io/netlify/368341f1-066a-43e9-9a30-dcbc2ac3e61e?color=green&label=Docs&style=flat-square)](https://zenora.netlify.app/)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ahnaf-zamil/zenora?include_prereleases&style=flat-square)](https://github.com/ahnaf-zamil/zenora/releases)
[![Maintainability](https://api.codeclimate.com/v1/badges/e556bee232469ff28415/maintainability?style=flat-square)](https://codeclimate.com/github/ahnaf-zamil/zenora/maintainability)
[![issues](https://img.shields.io/github/issues-raw/ahnaf-zamil/zenora?color=blueviolet&style=flat-square)](https://github.com/ahnaf-zamil/zenora/issues) [![CodeQL](https://img.shields.io/github/workflow/status/ahnaf-zamil/zenora/CodeQL?logo=GitHub&style=flat-square&label=CodeQL)](https://github.com/ahnaf-zamil/zenora/actions/workflows/codeql-analysis.yml)

A simple to use synchronous yet functional Discord REST API wrapper for Python

## What is Zenora

Zenora is a synchronous library for accessing the Discord REST API. It allows you to access the API without async/await. And also gives you REST-only API access, not the gateway. Pretty useful for making bot web dashboards, or desktop applications, etc. Oauth and other features will be added soon.

## Installation

Install from Git

```bash
pip install git+https://github.com/ahnaf-zamil/zenora
```

or install with pip

```bash
pip install Zenora
```

## Basic Usage

```python
from zenora import APIClient

client = APIClient(token="...")
# There is also a set_token method which can be used to replace the token later on

# Make API request to get the currently logged in user object
user = client.users.get_current_user()

# Use the data :D
print(user.username)
```

## Using Oauth

Zenora has can be used for accessing the Discord Oauth API (WIP). It is very simple to use, and reduces a lot
of the hassle for implementing Discord Oauth in your application. But before you do try out Zenora, you need to
know how to use get the authorization code from the Discord API in order to use it (this is mandatory and cannot be
avoided as Zenora depends on that code in order to get the access token).

Link: https://discord.com/developers/docs/topics/oauth2#authorization-code-grant

Once you have the authorization code, Zenora will do the rest of the work for you. Just call some functions and you will get your
access token and will be able to use that to with the Discord API.

Example:

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

# Query the user object that has used your Oauth application
user = bearer_client.users.get_current_user()

print(user) # Prints it out :)
```

## Documentation

The latest documentation is currently hosted [here](https://zenora.netlify.app/).

## Contributing

If you are considering to contribute, thanks a lot! We welcome all contributors here and, you can help out as well.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Before contributing, please check out our [CONTRIBUTING.md](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for more information.

## License

[MIT](https://choosealicense.com/licenses/mit/) License

Copyright (c) 2021 DevGuyAhnaf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
