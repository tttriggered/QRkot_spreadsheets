from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import (
    BaseUserManager, FastAPIUsers, IntegerIDMixin, InvalidPasswordException
)
from fastapi_users.authentication import (
    AuthenticationBackend, BearerTransport, JWTStrategy
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.constants import MIN_LENGTH_FOR_PASSWORD
from app.core.config import settings
from app.core.db import get_async_session
from app.models.user import User
from app.schemas.user import UserCreate


async def get_user_db(
        session: AsyncSession = Depends(get_async_session)
) -> SQLAlchemyUserDatabase:
    """Асинхронный генератор для доступа к базе данных через SQLAlchemy."""
    yield SQLAlchemyUserDatabase(session, User)


bearer_transport = BearerTransport(tokenUrl='auth/jwt/login')


def get_jwt_strategy() -> JWTStrategy:
    """Возвращает JWT стратегию с секретом и временем жизни."""
    return JWTStrategy(secret=settings.secret, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """
    Менеджер пользователей для управления пользователями и их паролями.
    """

    async def validate_password(
            self,
            password: str,
            user: Union[UserCreate, User]
    ) -> None:
        """
        Проверяет корректность пароля пользователя.
        """
        if len(password) < MIN_LENGTH_FOR_PASSWORD:
            raise InvalidPasswordException(
                reason='Пароль должен содержать не менее 3 символов'
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason='Пароль не должен содержать e-mail'
            )

    async def on_after_register(
            self, user: User, request: Optional[Request] = None
    ):
        """Обрабатывает действия после регистрации пользователя."""
        print(f'Пользователь {user.email} зарегистрирован.')


async def get_user_manager(user_db=Depends(get_user_db)) -> UserManager:
    """Возвращает менеджера пользователей для работы с базой данных."""
    yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

# Получение текущего активного пользователя
current_user = fastapi_users.current_user(active=True)

# Получение текущего активного суперпользователя
current_superuser = fastapi_users.current_user(active=True, superuser=True)
