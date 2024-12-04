import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "28243586"))
  API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7668383218:AAEcv8G-D9RoPvP65_Rbdm0Q1-A-S4rAD2Y")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "UR_Yorha_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002356823829"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "modijiurl.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "294f4eb777a2c0018baaf6b719e10872ae8cb33e")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "7357726710"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://smkbotz:69ufNrjYoMhDDMUL@cluster0.1fw9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002332051361")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002328437358"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
ʟᴏᴠᴇ ʜᴇɴᴛᴀɪ? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀᴛᴄʜ ᴡʜᴀᴛ ʏᴏᴜ'ʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.

ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ʙᴇʟᴏᴡ ꜰᴏʀ ᴍᴏʀᴇ!👇

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/)
"""
  HOME_TEXT = """
ʟᴏᴠᴇ ʜᴇɴᴛᴀɪ? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀᴛᴄʜ ᴡʜᴀᴛ ʏᴏᴜ'ʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.

ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ʙᴇʟᴏᴡ ꜰᴏʀ ᴍᴏʀᴇ!👇
"""
