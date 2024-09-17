from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    Модель пользователя для таблицы базы данных.

    Наследует от `SQLAlchemyBaseUserTable`
    для интеграции с системой аутентификации
    и от `Base` для поддержки функционала SQLAlchemy ORM.

    Атрибуты:
        id (int): Уникальный идентификатор пользователя.
        email (str): Электронная почта пользователя.
        hashed_password (str): Хэш пароля пользователя.
        is_active (bool): Флаг активности пользователя.
        is_superuser (bool): Флаг суперпользователя.
        is_verified (bool): Флаг подтверждения электронной почты.
    """
    pass
