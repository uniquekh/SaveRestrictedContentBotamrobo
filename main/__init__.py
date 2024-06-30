#Github.com/8769Anurag

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("21179966", default=None, cast=int)
API_HASH = config("d97919fb0a3c725e8bb2a25bbb37d57c", default=None)
BOT_TOKEN = config("6710743479:AAF1-A8-2tMhzVUP36cYuTA-1q0_vVabmqs", default=None)
SESSION = config("AQFDLj4ApMgN1F2qrTOYApAsFbYnNBGVVaM2M0tXSGoX-vZ8DExtV7WRxpRo2VdD8IGYV1hn6abC17fX-CY9TgqlfQ1dVKVewD57MBDCJSmj3euOBAwjP7SH0mEGygdlH_WpihZFBp0BMM2VUSTc07IP-0EKR_Nmv0dqMj90mgLSRNJ5MHJV94-XiDWGszYj8fZgdZrczwDuWuhpMnW6PDIXt9T6vbZqgbk85p_cWmYzwf1boL1hnQx-0nqDMU7IOMcp8MG5InRxl1lM0SeVVCU1UMff8ZDkeh0aemYFLHAeQQo9eZ4vDDPesG9CCX7f4k7RrGmafVuXpAmCZ3XIVjRdpmR2_AAAAAG0r_Q_AA", default=None)
FORCESUB = config("@getallmodapk", default=None)
AUTH = config("7326397503", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
