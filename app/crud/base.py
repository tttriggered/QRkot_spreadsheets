from typing import Optional

from sqlalchemy import select, literal_column
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User


class CRUDBase:
    """Базовый класс для CRUD-операций с моделями."""

    def __init__(self, model):
        """Инициализирует класс с моделью."""
        self.model = model

    async def get_multi(self, session: AsyncSession):
        """Получить список объектов из базы данных."""
        result = await session.execute(select(self.model))
        return result.scalars().all()

    async def get(self, obj_id: int, session: AsyncSession):
        """Получить объект по его ID."""
        result = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return result.scalars().first()

    async def create(self, obj_in, session: AsyncSession,
                     user: Optional[User] = None, commit: bool = True):
        """Создать новый объект в базе данных."""
        obj_data = obj_in.dict()
        if user:
            obj_data['user_id'] = user.id
        db_obj = self.model(**obj_data)
        session.add(db_obj)
        if commit:
            await session.commit()
            await session.refresh(db_obj)
        return db_obj

    async def update(self, db_obj, obj_in, session: AsyncSession,
                     commit: bool = True):
        """Обновить данные объекта в базе данных."""
        updates = obj_in.dict(exclude_unset=True)
        for field, value in updates.items():
            setattr(db_obj, field, value)
        session.add(db_obj)
        if commit:
            await session.commit()
            await session.refresh(db_obj)
        return db_obj

    async def remove(self, db_obj, session: AsyncSession):
        """Удалить объект из базы данных."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_not_invested(self, session: AsyncSession):
        """
        Получить не проинвестированные объекты,
        отсортированные по дате создания.
        """
        result = await session.execute(
            select(self.model)
            .where(self.model.fully_invested.is_(literal_column('false')))
            .order_by(self.model.create_date)
        )
        return result.scalars().all()

    async def get_status_by_id(self, object_id: int, session: AsyncSession):
        """Получить статус объекта по ID."""
        result = await session.execute(
            select(self.model.fully_invested).where(self.model.id == object_id)
        )
        return result.scalars().first()

    async def get_invested_amount_by_id(self, object_id: int,
                                        session: AsyncSession):
        """Получить сумму инвестиций по ID объекта."""
        result = await session.execute(
            select(self.model.invested_amount).where(
                self.model.id == object_id)
        )
        return result.scalars().first()
