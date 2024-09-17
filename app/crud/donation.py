from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import User
from app.models.donation import Donation


class CRUDDonation(CRUDBase):
    """
    Класс для выполнения CRUD-операций над моделью Donation.
    Наследует базовые CRUD-операции из CRUDBase.
    """

    @staticmethod
    async def get_by_user(user: User, session: AsyncSession):
        """
        Получить список донатов, связанных с указанным пользователем.
        """
        result = await session.execute(
            select(Donation).where(Donation.user_id == user.id)
        )
        return result.scalars().all()


donation_crud = CRUDDonation(Donation)