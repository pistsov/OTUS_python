from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from models import Post


async def create_user(
    session: AsyncSession,
    username: str,
    name: str,
    email: str
) -> User:
    user = User(name=name, username=username, email=email)

    session.add(user)
    await session.commit()


async def create_post(session: AsyncSession, post_title: str, post_body: str, user_id: User) -> Post:
    post = Post(
        title=post_title,
        body=post_body,
        user_id=user_id,
    )

    session.add(post)
    await session.commit()


async def populate_users(session: AsyncSession, users_data: dict) -> None:
    for user in users_data:
        await create_user(
            session=session,
            username=user.get("username"),
            name=user.get("name"),
            email=user.get("email")
        )


async def populate_posts(session: AsyncSession, posts_data: dict) -> None:
    for post in posts_data:
        await create_post(
            session=session,
            post_title=post.get("title"),
            post_body=post.get("body"),
            user_id=post.get("userId")
        )
