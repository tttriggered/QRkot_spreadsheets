from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, Extra, PositiveInt

from app.schemas.constants import MAX_NAME_LENGTH, MIN_STRING_LENGTH


class CharityProjectBase(BaseModel):
    """Базовая модель для благотворительного проекта."""

    name: Optional[str] = Field(None, max_length=MAX_NAME_LENGTH)
    description: Optional[str] = Field(None)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid
        min_anystr_length = MIN_STRING_LENGTH


class CharityProjectCreate(CharityProjectBase):
    """Модель для создания нового благотворительного проекта."""

    name: str = Field(..., max_length=MAX_NAME_LENGTH)
    description: str = Field(...)
    full_amount: PositiveInt

    class Config:
        min_anystr_length = MIN_STRING_LENGTH


class CharityProjectUpdate(CharityProjectBase):
    """Модель для обновления данных благотворительного проекта."""
    pass


class CharityProjectDB(CharityProjectCreate):
    """Модель для представления благотворительного проекта в базе данных."""

    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
