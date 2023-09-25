"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

import crud
from models import Base, engine, async_engine, Session
from jsonplaceholder_requests import fetch_users, fetch_posts


async def async_main():
    async with async_engine.begin() as session:
        await session.run_sync(Base.metadata.drop_all)
        await session.run_sync(Base.metadata.create_all)
    async with Session() as session:  # type: AsyncSession
        users_data, posts_data = await asyncio.gather(
            fetch_users(),
            fetch_posts()
        )
        await crud.populate_users(session, users_data)
        await crud.populate_posts(session, posts_data)
    # async with async_engine.begin() as session:
    #     await session.run_sync(Base.metadata.drop_all)


def main():
    asyncio.run(async_main())


if __name__ == '__main__':
    main()
