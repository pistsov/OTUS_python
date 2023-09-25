from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    create_engine
)
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DB_URL = "postgresql+pg8000://postgres:secretpassword@0.0.0.0:5432/postgres"
ASYNC_DB_URL = "postgresql+asyncpg://postgres:secretpassword@0.0.0.0:5432/postgres"
DB_ECHO = False
# DB_ECHO = True

engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO,
)

async_engine = create_async_engine(
    url=ASYNC_DB_URL,
    echo=DB_ECHO,
)

Session = sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=False)
    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )
