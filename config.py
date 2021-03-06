import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 1234567))
    API_HASH = os.environ.get("API_HASH", "")
    # Your Updates channel username 
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Google drive folder id
    parent_id = os.environ.get("GDRIVE_FOLDER_ID","")
    # Set True is drive folder id is Team Drive
    IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", True)
    # Set it True if using Service Account for uploading
    USE_SERVICE_ACCOUNTS = os.environ.get("USE_SERVICE_ACCOUNTS", False)
    # Your gdrive index url (Important)
    INDEX_URL = os.environ.get("INDEX_URL", "")
