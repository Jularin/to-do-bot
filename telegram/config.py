import os

from dotenv import load_dotenv

load_dotenv()

#We take the tokken of the bot, which is registered in the .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')
