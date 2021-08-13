from urllib.parse import quote

PORT = 5000
BOT_TOKEN = "put your bot token here"
CLIENT_SECRET = "put your bot's client secret here"
CLIENT_ID = 123456789  # Enter your bot's client ID
REDIRECT_URI = (
    f"http://localhost:{PORT}/oauth/callback"  # Your Oauth redirect URI
)
OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={quote(REDIRECT_URI)}&response_type=code&scope=identify"
