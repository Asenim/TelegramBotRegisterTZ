from settings import Client, logger
from pyrogram.types import Message
from asyncio import sleep
import os
from working_with_db import insert_db
import datetime


async def user_send_messages(client_api: Client, message: Message):
    logger.info(f'{message.text}, {message.from_user.username}')
    user_id = message.from_user.id
    user_name = message.from_user.username
    path_in_foto = os.path.abspath("photo_materials/cat_in_box.png")
    time_registration = datetime.date.today()
    await insert_db.insert_user_in_db(uu_id=user_id, user_name=user_name, date_inserted=time_registration)
    # await find_trigger_message(client=client_api, message=message)
    await sleep(1)
    await client_api.send_message(chat_id=message.chat.id, reply_to_message_id=message.id, text=f'Добрый день {user_name}!')
    await sleep(3)
    await client_api.send_message(chat_id=message.chat.id, text=f'Подготовила для вас материал')
    await client_api.send_photo(chat_id=message.chat.id, photo=f'{path_in_foto}')
    # date = message.date.time()
    # message_id = message.id
    # message_chat_user = message.chat.username
    # message_user = message.from_user.id
    # print(date, message_id, message_chat_user, message_user)


# async def find_trigger_message(client, message):
#     async for messages in client.get_chat_history(chat_id=message.chat.id):
#         if messages.text == 'Хорошего дня':
#             print(messages.id, messages.date, messages.text, messages.from_user.username)
