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
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6564513574:AAHsUNXeDK0rk6uDrdi37MgYKJ7gIqo1Yho")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "DemoVJ_Bot")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "20389440"))
    API_HASH = os.environ.get("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
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
    OWNER_ID = int(os.environ.get("OWNER_ID", "6168162777"))
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER", "6168162777")

    VERIFY = bool(environ.get('VERIFY', True))
    SHORTLINK_URL = environ.get('SHORTLINK_URL', 'moneykamalo.com')
    SHORTLINK_API = environ.get('SHORTLINK_API', '0eefb93e1e3ce9470a7033115ceb1bad13a9d674')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001623633000"))
