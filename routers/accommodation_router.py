from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db_manager_factory import get_db_manager

router = APIRouter()

db_manager = get_db_manager()

class AccommodationCreate(BaseModel):
    student_id: int
    room_id: int
    date_assigned: str

class AccommodationResponse(BaseModel):
    id: int
    student_id: int
    room_id: int
    date_assigned: str

    class Config:
        orm_mode = True

@router.post("/", response_model=AccommodationResponse)
def create_accommodation(accommodation: AccommodationCreate):
    db_manager.accommodations.add_accommodation(**accommodation.dict())
    return db_manager.accommodations.get_all_accommodations()[-1]

@router.get("/", response_model=list[AccommodationResponse])
def read_accommodations():
    return db_manager.accommodations.get_all_accommodations()

@router.get("/{accommodation_id}", response_model=AccommodationResponse)
def read_accommodation(accommodation_id: int):
    accommodation = db_manager.accommodations.get_accommodation_by_id(accommodation_id)
    if not accommodation:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    return accommodation

@router.put("/{accommodation_id}", response_model=AccommodationResponse)
def update_accommodation(accommodation_id: int, accommodation: AccommodationCreate):
    db_manager.accommodations.update_accommodation(accommodation_id, **accommodation.dict())
    return db_manager.accommodations.get_accommodation_by_id(accommodation_id)

@router.delete("/{accommodation_id}", response_model=AccommodationResponse)
def delete_accommodation(accommodation_id: int):
    accommodation = db_manager.accommodations.get_accommodation_by_id(accommodation_id)
    if not accommodation:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    db_manager.accommodations.delete_accommodation(accommodation_id)
    return accommodation
