from pyrogram import Client, idle
from dotenv import load_dotenv
import os
from loguru import logger

logger.add('debug.log', format='{time} {level} {message}', level='INFO', rotation='1000 KB', compression='zip')
load_dotenv()
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
API_TOKEN = os.environ.get("API_TOKEN")
# ID чата который будем слушать (Нужен исключительно для того что бы работать вне Бота)
MAIN_CHAT_ID = os.environ.get("MAIN_CHAT_ID")
# ID владельца чата Можно достать из id_chat_bot (Обязательный параметр,
# нужен, что бы бот понимал кто является владельцем чата)
ADMIN_CHAT_ID = os.environ.get("CHAT_ADMIN_ID")
# username вашего чата (заканчивается на _bot, можно посмотреть в профиле, вводите без @)
CHAT_USER_NAME = os.environ.get("CHAT_USER_NAME")

POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')


client = Client(name="Client_bot", api_id=api_id, api_hash=api_hash, bot_token=API_TOKEN)
