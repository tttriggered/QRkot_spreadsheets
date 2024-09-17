from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime, CheckConstraint

from app.core.db import Base
from app.models.constants_for_models import REPR_TEMPLATE


class BaseCharity(Base):
    __abstract__ = True
    __table_args__ = (
        CheckConstraint('full_amount > 0'),
        CheckConstraint(
            'invested_amount >= 0',
            'invested_amount <= full_amount'
        ),
    )
    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    close_date = Column(DateTime)

    def __repr__(self):
        return REPR_TEMPLATE.format(
            full_amount=self.full_amount,
            invested_amount=self.invested_amount,
            fully_invested=self.fully_invested,
            create_date=self.create_date,
            close_date=self.close_date
        )
