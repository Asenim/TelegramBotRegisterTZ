from models import *
import datetime


async def select_from_db():
    """
    Делает выборку по дате добавления
    :return query: объект запроса
    """
    async with get_session() as session:
        today_data = datetime.date.today()

        __user = users_table.select().where(users_table.c.RegisterDate == today_data)
        query = await session.execute(__user)
        return query
