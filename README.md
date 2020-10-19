# Zenora.py

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![](https://travis-ci.org/ahnaf-zamil/zenora.svg?branch=master) ![Pypi](https://img.shields.io/pypi/v/zenora.svg)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ahnaf-zamil/zenora?include_prereleases) [![docs](https://img.shields.io/badge/documentation-up-00FF00.svg)](https://zenora-py.github.io) [![issues](https://img.shields.io/github/issues-raw/ahnaf-zamil/zenora)](https://github.com/ahnaf-zamil/zenora/issues) [![prs](https://img.shields.io/github/issues-pr/ahnaf-zamil/zenora)](https://github.com/ahnaf-zamil/zenora/pulls) [![pyvers](https://img.shields.io/pypi/pyversions/zenora)](https://pypi.org/project/zenora)

[![Discord](https://discord.com/api/guilds/753859568764977194/widget.png?style=banner2)](https://discord.gg/2Buh3N9)

A modern Discord REST API wrapper that allows you to access the data without running a bot.

## Installation

Use Git to clone Zenora's source code

```bash
git clone https://github.com/ahnaf-zamil/zenora
```

Or

Install from PyPi

```bash
python -m pip install zenora
```

## Usage

```python

# Import the library
import zenora

# Instantiate a REST API instance
api = zenora.REST(token="your_token_here", token_type="token_type")

# Query API for getting the current user's info
# Zenora parses API response into Python objects for accessing data
user = api.get_current_user()

# Use the data
print(user.name)

```

## Documentation

Check out the documentation at https://zenora-py.github.io

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate. Check the [contributing.md](https://github.com/ahnaf-zamil/zenora/blob/master/CONTRIBUTING.md) file for more info.

## Community

Wanna hang out or collaborate with other contributers?
Join the official Discord server [here.](https://discord.gg/2Buh3N9)

## License

[MIT](https://choosealicense.com/licenses/mit/) License

Copyright (c) 2020 K.M Ahnaf Zamil and Maksym Karunos

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
