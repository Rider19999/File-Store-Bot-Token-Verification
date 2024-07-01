# Thanks @Codeflix_Bots

import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7488352337:AAH4cyI-ORSCGwntUB2jWEdlGvmFXoLmrfA")

APP_ID = int(os.environ.get("APP_ID", "25303461"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "abe6bf86f47e49752225d555284d27bd")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002053305284"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6036448711"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://susantamusic:susantabhan@cluster0.5pwi1py.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "paisakamalo.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "8cd309cdcc4540facb9b0e8ea99088df38b3f8e6")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/HowToDownloadMovieRk/3")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002037440123"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n ɪ ᴀᴍ ᴛᴏᴋᴇɴ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ , ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ » @team_netflix</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6036448711").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} 𝐁𝐫𝐨/𝐒𝐢𝐬 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬..\n\n 𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐟𝐢𝐫𝐬𝐭 𝐚𝐧𝐝 𝐜𝐥𝐢𝐜𝐤 𝐨𝐧 “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @RkMovie_Channel</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🔞  𝐖𝐚𝐭𝐜𝐡 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐀𝐝𝐮𝐥𝐭 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 🔞\n\n⭕ https://t.me/Adult_Zonn"

ADMINS.append(OWNER_ID)
ADMINS.append(6036448711)

LOG_FILE_NAME = "codeflixbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
