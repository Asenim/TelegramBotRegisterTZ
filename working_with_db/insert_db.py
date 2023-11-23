from models import *


async def insert_user_in_db(uu_id, user_name, date_inserted):
    """
    Добавляет нового пользователя в БД
    :param uu_id: UUID уникальный user id пользователя (message.from_user.id)
    :param user_name: user name пользователя телеграм (message.from_user.username)
    :param date_inserted: Дата когда пользователь зарегестрировался
    :return:
    """
    async with get_session() as session:
        exist = await check_record_existence(conn=session, uu_id=uu_id)
        if exist:
            print('Пользователь с таким user id существует в таблице')
        else:
            __user = users_table.insert().values(UUID=uu_id, UserName=user_name, RegisterDate=date_inserted)
            last_record_id = await session.execute(__user)
            await session.commit()

            print('Запись добавлена в таблицу')
            return __user, last_record_id


async def check_record_existence(conn, uu_id):
    """
    Сопрограмма для проверки наличия записи в БД
    :param conn: объект session/connection
    :param uu_id: UUID уникальный user id пользователя (message.from_user.id)
    :return bool:
    """
    query = users_table.select().where(users_table.c.UUID == uu_id)
    result = await conn.execute(query)
    record_exists = result.first()
    if record_exists:
        return True
    else:
        return False
