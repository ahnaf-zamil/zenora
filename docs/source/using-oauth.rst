===============
Using Oauth
===============

Zenora has can be used for accessing the Discord Oauth API. It is very simple to use, and reduces a lot
of the hassle for implementing Discord Oauth in your application. But before you do try out Zenora, you need to
know how to use get the authorization code from the Discord API in order to use it (this is mandatory and cannot be
avoided as Zenora depends on that code in order to get the access token).

Link: https://discord.com/developers/docs/topics/oauth2#authorization-code-grant

Once you have the authorization code, Zenora will do the rest of the work for you. Just call some functions and you will get your 
access token and will be able to use that to with the Discord API.

Usage
=======================
::

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
    user = bearer_client.get_current_user()

    print(user) # Prints it out :)
    


