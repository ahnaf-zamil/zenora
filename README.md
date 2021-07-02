# Zenora

![License: MIT](https://img.shields.io/badge/License-MIT-pink.svg)[![prs](https://img.shields.io/github/issues-pr/ahnaf-zamil/zenora)](https://github.com/ahnaf-zamil/zenora/pulls)
![Pypi](https://img.shields.io/pypi/v/zenora.svg)
![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-black)[![pyvers](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue)](https://pypi.org/project/zenora)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ahnaf-zamil/zenora?include_prereleases)[![issues](https://img.shields.io/github/issues-raw/ahnaf-zamil/zenora)](https://github.com/ahnaf-zamil/zenora/issues)

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

## Usage

```python
from zenora import APIClient

client = APIClient(token="...")
# There is also a set_token method which can be used to replace the token later on

# Make API request to get the currently logged in user object
user = client.users.get_current_user()

# Use the data :D
print(user.username)
```

## Documentation

The latest documentation is currently hosted [here](https://zenora.readthedocs.io/en/latest/).

## Contributing

If you are considering to contribute, thanks a lot! We welcome all contributors here and, you can help out as well.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Before contributing, please check out our [CONTRIBUTING.md](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for more information.

## License

[MIT](https://choosealicense.com/licenses/mit/) License

Copyright (c) 2021 K.M Ahnaf Zamil

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
