from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt, Extra


class DonationBase(BaseModel):
    """Базовая модель для пожертвования."""

    full_amount: PositiveInt
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    """Модель для создания пожертвования."""
    pass


class DonationShortDB(DonationBase):
    """Модель для краткого представления пожертвования в базе данных."""

    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationFullDB(DonationShortDB):
    """Модель для полного представления пожертвования в базе данных."""

    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
