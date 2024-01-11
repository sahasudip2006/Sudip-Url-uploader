import os
import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6535249965:AAH2BM6qVqVvFJ-YyrUMV0qFJNwshn-WVP4")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "S_url_uploader_bot")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "12596147"))
    API_HASH = os.environ.get("API_HASH", "376d2b9215aad81b9522afccd1067786")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "5165943027"))
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER", "5165943027")

    VERIFY = bool(environ.get('VERIFY', True)
    SHORTLINK_URL = environ.get('SHORTLINK_URL', 'mdisk.pro')
    SHORTLINK_API = environ.get('SHORTLINK_API', 'ee2e50b000e88ab6549ce6ade5313149a9851577')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001565949579"))
    TUTORIAL = os.environ.get("TUTORIAL", "https://t.me/main_channel_bot_update")
