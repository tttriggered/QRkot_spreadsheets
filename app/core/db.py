from typing import AsyncGenerator

from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr

from app.core.config import settings


class PreBase:
    """Базовый класс моделей с автоматическим названием таблицы."""

    @declared_attr
    def __tablename__(cls):
        """Название таблицы на основе имени класса в нижнем регистре."""
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Асинхронный генератор сессий для работы с базой данных."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
