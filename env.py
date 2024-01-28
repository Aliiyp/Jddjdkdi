import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("22127557", "").strip()
API_HASH = os.getenv("348f141a89ba55603d4c9360de9c5625", "").strip()
BOT_TOKEN = os.getenv("6382098188:AAE-16JoJ2RNX6FIO-nuLe8N-AhekOip5Sk", "").strip()
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split()))
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
