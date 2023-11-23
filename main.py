from settings import *
from pyrogram.handlers import MessageHandler
from pyrogram import filters
from pyrogram.types import BotCommand
from botAPI.user_send_message import user_send_messages
from botAPI.admin_send_command import admin_send_command


# Регистрация Хэндлера
client.add_handler(MessageHandler(admin_send_command, filters.command(commands='registered_in_today')))
client.add_handler(MessageHandler(user_send_messages))

bot_commands = [
    BotCommand(
        command='registered_in_today',
        description='Показывает всех зарегестрированных сегодня пользователей'
    )
]

# Запуск Клиента
client.start()
client.set_bot_commands(bot_commands)
idle()
client.stop()
