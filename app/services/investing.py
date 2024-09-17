from datetime import datetime
from typing import List

from app.models.base import BaseCharity


def investing(
        target: BaseCharity,
        sources: List[BaseCharity]
) -> List[BaseCharity]:
    """Процесс инвестирования: обновление сумм и статусов."""

    changed_sources = []
    target_investment = target.invested_amount if (target.invested_amount
                                                   is not None) else 0

    for source in sources:
        available_to_invest = min(
            source.full_amount - (source.invested_amount or 0),
            target.full_amount - target_investment
        )

        if available_to_invest <= 0:
            continue

        changed_sources.append(source)

        for entity in [target, source]:
            if entity.invested_amount is None:
                entity.invested_amount = 0
            entity.invested_amount += available_to_invest
            if entity.invested_amount >= entity.full_amount:
                entity.fully_invested = True
                entity.close_date = datetime.utcnow()

        if target.fully_invested:
            break

    return changed_sources
