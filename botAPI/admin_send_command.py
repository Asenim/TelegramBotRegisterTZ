from working_with_db import select_db
from settings import Client, ADMIN_CHAT_ID, MAIN_CHAT_ID
from pyrogram.types import Message


async def admin_send_command(client_api: Client, message: Message):
    # Инициализируем нужные переменные
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(user_id, chat_id)
    if user_id == int(ADMIN_CHAT_ID):
        # Получаем данные из БД
        data = await select_db.select_from_db()
        await client_api.send_message(chat_id=user_id, text=str(data.fetchall()))
