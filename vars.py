#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "28413721"))
API_HASH = environ.get("API_HASH", "c353284aee7154723e9766470434cf0a")
BOT_TOKEN = environ.get("BOT_TOKEN", "7260526992:AAH5VuX-loguHG8jp3hbwWt0C2D5F0nwvfI")
OWNER = int(environ.get("OWNER", "1860169540"))
CREDIT = "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
AUTH_USER = os.environ.get('AUTH_USERS', '1860169540').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
