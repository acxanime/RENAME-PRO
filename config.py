import os, re


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
OWNER = int(os.environ.get("OWNER", ""))
BOT_USERNAME = os.environ.get('BOT_USERNAME', "")

FORCE_SUBS = os.environ.get("FORCE_SUBS", "HxBots")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002031041556"))

DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "renamebot-premium")

STRING = os.environ.get("STRING", "")
BOT_PIC = os.environ.get("BOT_PIC", "https://graph.org/file/cca849a2f63053fa3f622.jpg")





# if you need to add verify system then dm me on telegram

SHORTNER_URL = os.environ.get("SHORTNER_URL", "arlinks.in")
SHORTNER_API = os.environ.get("SHORTNER_API", "b12d324481cefcfe34f8802dc8dab8a0a640d370")
TOKEN_TIMEOUT = os.environ.get("TOKEN_TIMEOUT", "40000")
