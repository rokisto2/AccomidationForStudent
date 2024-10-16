from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db_manager_factory import get_db_manager

router = APIRouter()

db_manager = get_db_manager()

class RoomCreate(BaseModel):
    dormitory_id: int
    room_type: str
    bed_count: int

class RoomResponse(BaseModel):
    id: int
    dormitory_id: int
    room_type: str
    bed_count: int

    class Config:
        orm_mode = True

@router.post("/", response_model=RoomResponse)
def create_room(room: RoomCreate):
    db_manager.rooms.add_room(**room.dict())
    return db_manager.rooms.get_all_rooms()[-1]

@router.get("/", response_model=list[RoomResponse])
def read_rooms():
    return db_manager.rooms.get_all_rooms()

@router.get("/{room_id}", response_model=RoomResponse)
def read_room(room_id: int):
    room = db_manager.rooms.get_room_by_id(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.put("/{room_id}", response_model=RoomResponse)
def update_room(room_id: int, room: RoomCreate):
    db_manager.rooms.update_room(room_id, **room.dict())
    return db_manager.rooms.get_room_by_id(room_id)

@router.delete("/{room_id}", response_model=RoomResponse)
def delete_room(room_id: int):
    room = db_manager.rooms.get_room_by_id(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    db_manager.rooms.delete_room(room_id)
    return room
