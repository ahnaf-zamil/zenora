===============
Getting Started
===============

Zenora can be installed be Python's package manager, pip:

``$ pip install zenora``

.. note::
    This library is dependent on Requests and so naturally will only be available for Python
    versions that Requests also supports.


Accessing the API
=======================

Your first API usage can be written in just a few lines of code:
::

    # Import the library
    import zenora

    # Instantiate a REST API instance
    api = zenora.REST(token="your_token_here", token_type="Your token type")

    # Query API for getting the current user's info
    # Zenora parses API response into Python objects for accessing data
    user = api.get_current_user()

    # Use the data
    print(user.name)

.. note::
    There are two types of tokens used by the Discord API. Those are the ``Bearer`` and ``Bot`` tokens.
    The ``Bearer`` token is used for Oauth2 applications while the ``Bot`` token is used for bot applications
    and scripts.