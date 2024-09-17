import contextlib

from fastapi_users.exceptions import UserAlreadyExists
from pydantic import EmailStr

from app.core.config import settings
from app.core.db import get_async_session
from app.core.user import get_user_db, get_user_manager
from app.schemas.user import UserCreate

get_async_session_ctx = contextlib.asynccontextmanager(get_async_session)
get_user_db_ctx = contextlib.asynccontextmanager(get_user_db)
get_user_manager_ctx = contextlib.asynccontextmanager(get_user_manager)


async def create_user(email: EmailStr, password: str,
                      is_superuser: bool = False):
    """Создаёт пользователя с заданными параметрами."""
    try:
        async with get_async_session_ctx() as session:
            async with get_user_db_ctx(session) as user_db:
                async with get_user_manager_ctx(user_db) as user_manager:
                    user_create_data = UserCreate(
                        email=email,
                        password=password,
                        is_superuser=is_superuser
                    )
                    await user_manager.create(user_create_data)
    except UserAlreadyExists:
        pass


async def create_first_superuser():
    """Создаёт первого суперпользователя, если указаны email и пароль."""
    email = settings.first_superuser_email
    password = settings.first_superuser_password

    if email and password:
        await create_user(
            email=email,
            password=password,
            is_superuser=True
        )
