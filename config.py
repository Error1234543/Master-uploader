import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8483889672:AAHF218gaOzYjnoarBrJhNylBmw2C2H65CE")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "20619533"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "5893568858a096b7373c1970ba05e296")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "8226637107").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
