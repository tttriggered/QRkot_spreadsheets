from sqlalchemy import Column, String, Text

from app.models.base import BaseCharity
from app.models.constants_for_models import REPR_FORMAT, MAX_REPR_LENGTH


class CharityProject(BaseCharity):
    """Модель благотворительных проектов фонда."""
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return REPR_FORMAT.format(
            name=self.name[:MAX_REPR_LENGTH],
            description=self.description[:MAX_REPR_LENGTH],
            super=super().__repr__()
        )
