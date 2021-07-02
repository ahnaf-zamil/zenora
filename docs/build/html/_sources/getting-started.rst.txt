===============
Getting Started
===============

Zenora can be installed be Python's package manager, pip:

``pip install git+https://github.com/ahnaf-zamil/zenora``

.. note::
    This library is dependent on Requests and so naturally will only be available for Python
    versions that Requests also supports.


Usage
=======================
::

    from zenora import APIClient

    client = APIClient(token="...")
    # There is also a set_token method which can be used to replace the token later on

    # Make API request to get the currently logged in user object
    user = client.users.get_current_user()

    # Use the data :D
    print(user.username)
