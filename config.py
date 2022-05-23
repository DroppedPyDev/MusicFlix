import os

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
ADMIN = int(os.getenv('ADMIN',1981831553)) # Here Given Creator Id , Replace it with your ID.
CHANNEL = int(os.getenv('CHANNEL',12345))
API_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
BOT_USERNAME = os.getenv("BOT_USERNAME", "Aami_song_bot")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "readmeab")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "readmeab")
SOURCE_CODE = os.getenv("SOURCE_CODE", "github.com/username")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# എന്താടാ മോനെ അടിച്ചു അടിച്ചു മാറ്റാൻ വന്നതാണോ? നാണം വേണം കേട്ടോ കുറച്ച് 😜😹.
# എന്തായാലും എടുത്തു bug ആരികും മുഴുവൻ നോക്കി ഒക്കെ add ആക്ക് കേട്ടോ 🤭
