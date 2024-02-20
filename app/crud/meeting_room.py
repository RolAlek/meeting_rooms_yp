from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.meeting_room import MeetingRoom
from app.schemas.meeting_room import MeetingRoomCreate, MeetigRoomUpdate


async def create_meeting_room(
    new_room: MeetingRoomCreate,
    session: AsyncSession,
) -> MeetingRoom:
    """Создает и возвращает объект переговорной комнаты."""
    new_room_data = new_room.dict()

    db_room = MeetingRoom(**new_room_data)

    session.add(db_room)
    await session.commit()
    await session.refresh(db_room)

    return db_room


async def read_all_rooms_from_db(session: AsyncSession) -> list[MeetingRoom]:
    all_rooms = await session.execute(select(MeetingRoom))
    all_rooms = all_rooms.scalars().all()
    return all_rooms


async def update_meeting_room(
    db_room: MeetingRoom,
    room_in: MeetigRoomUpdate,
    session: AsyncSession
) -> MeetingRoom:
    obj_data = jsonable_encoder(db_room)
    update_data = room_in.dict(exclude_unset=True)

    for field in obj_data:
        if field in update_data:
            setattr(db_room, field, update_data[field])

    session.add(db_room)
    await session.commit()
    await session.refresh(db_room)
    return db_room


async def get_meeting_room_by_id(
    room_id: int,
    session: AsyncSession
) -> Optional[MeetingRoom]:
    db_room = await session.get(MeetingRoom, room_id)
    return db_room


async def get_room_id_by_name(
    room_name: str,
    session: AsyncSession
) -> Optional[int]:
    """Получает из БД id переговорной комнаты и возвращает его."""
    db_room_id = await session.execute(
        select(MeetingRoom.id).where(MeetingRoom.name == room_name)
    )
    db_room_id = db_room_id.scalars().first()
    return db_room_id


async def delete_meeting_room(
    db_room: MeetingRoom,
    session: AsyncSession
) -> MeetingRoom:
    await session.delete(db_room)
    await session.commit()
    return db_room
