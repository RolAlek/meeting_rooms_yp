from datetime import datetime

from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.services.google_api import (
    spreadsheets_create, set_user_permissions, spreadsheets_update_value
)
from app.core.user import current_superuser
from app.crud import reservation_crud


router = APIRouter()


@router.post(
    path='/',
    response_model=list[dict[str, int]],
    dependencies=[Depends(current_superuser)]
)
async def get_report(
    from_reserve: datetime,
    to_reserve: datetime,
    session: AsyncSession = Depends(get_async_session),
    wrapper_services: Aiogoogle = Depends(get_service)
):
    """Только для суперюзеров."""
    reservations = await reservation_crud.get_count_res_at_the_same_time(
        from_reserve, to_reserve, session
    )
    spreadsheet_id = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheet_id, wrapper_services)
    await spreadsheets_update_value(
        spreadsheet_id, reservations, wrapper_services
    )
    return reservations
