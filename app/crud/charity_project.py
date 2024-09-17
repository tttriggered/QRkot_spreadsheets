from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    """
    Класс для операций CRUD над моделью CharityProject.
    Наследует базовые CRUD-операции из CRUDBase.
    """

    @staticmethod
    async def get_project_id_by_name(project_name: str,
                                     session: AsyncSession) -> Optional[int]:
        """
        Возвращает ID проекта по его названию.
        """
        result = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name)
        )
        return result.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)
