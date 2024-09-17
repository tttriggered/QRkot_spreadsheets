from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models.base import BaseCharity
from app.models.constants_for_models import REPR_FORMAT_USER, MAX_REPR_LENGTH


class Donation(BaseCharity):
    """Модель пожертвований в фонд."""
    user_id = Column(Integer,
                     ForeignKey('user.id',
                                name='fk_donation_user_id_user'))
    comment = Column(Text)

    def __repr__(self):
        return REPR_FORMAT_USER.format(
            user_id=self.user_id,
            comment=self.comment[:MAX_REPR_LENGTH],
            super=super().__repr__()
        )
