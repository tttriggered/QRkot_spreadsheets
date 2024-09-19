from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.constants_for_api import (PROJECT_NOT_FOUND,
                                       DUPLICATE_PROJECT_NAME,
                                       INVESTMENT_AMOUNT_TOO_LOW,
                                       PROJECT_HAS_FUNDING,
                                       CLOSED_PROJECT_EDIT)
from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_project_exists(project_id: int, session: AsyncSession) -> (
        CharityProject):
    """Проверка существования проекта по идентификатору."""

    project = await charity_project_crud.get(project_id, session)

    if project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=PROJECT_NOT_FOUND
        )

    return project


async def check_name_duplicate(project_name: str,
                               session: AsyncSession) -> None:
    """Проверка уникальности названия проекта."""

    project_id = await charity_project_crud.get_project_id_by_name(
        project_name, session
    )

    if project_id:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=DUPLICATE_PROJECT_NAME
        )


async def check_new_full_amount_bigger_than_invested_amount(
        project_id: int,
        new_full_amount: int,
        session: AsyncSession):
    """Проверка, что новая сумма больше уже инвестированной."""

    invested_amount = await charity_project_crud.get_invested_amount_by_id(
        project_id, session
    )

    if invested_amount > new_full_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=INVESTMENT_AMOUNT_TOO_LOW
        )

    return invested_amount


async def check_project_already_got_donation(project_id: int,
                                             session: AsyncSession) -> None:
    """Проверка, что проект уже получил финансирование."""

    invested_amount = await charity_project_crud.get_invested_amount_by_id(
        project_id, session
    )

    if invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=PROJECT_HAS_FUNDING
        )

    return invested_amount


async def check_project_is_closed(project_id: int,
                                  session: AsyncSession) -> bool:
    """Проверка, закрыт ли проект."""

    project_status = await charity_project_crud.get_status_by_id(
        project_id, session
    )

    if project_status:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=CLOSED_PROJECT_EDIT
        )

    return project_status
