import os
from dotenv import load_dotenv


load_dotenv()
BOT_tOKEN = os.getenv("BOT_TOKEN")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "yakuza_bot")

ADMINS = ['7929208588', '1877208776', '8331923778']
