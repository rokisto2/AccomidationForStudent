from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db_manager_factory import get_db_manager

router = APIRouter()

db_manager = get_db_manager()

class AdministrationCreate(BaseModel):
    name: str
    assigned_dormitory_id: int
    work_done: str  # отработки

class AdministrationResponse(BaseModel):
    id: int
    name: str
    assigned_dormitory_id: int
    work_done: str

    class Config:
        orm_mode = True

@router.post("/", response_model=AdministrationResponse)
def create_administration(administration: AdministrationCreate):
    db_manager.administrations.add_administration(**administration.dict())
    return db_manager.administrations.get_all_administrations()[-1]

@router.get("/", response_model=list[AdministrationResponse])
def read_administrations():
    return db_manager.administrations.get_all_administrations()

@router.get("/{administration_id}", response_model=AdministrationResponse)
def read_administration(administration_id: int):
    administration = db_manager.administrations.get_administration_by_id(administration_id)
    if not administration:
        raise HTTPException(status_code=404, detail="Administration not found")
    return administration

@router.put("/{administration_id}", response_model=AdministrationResponse)
def update_administration(administration_id: int, administration: AdministrationCreate):
    db_manager.administrations.update_administration(administration_id, **administration.dict())
    return db_manager.administrations.get_administration_by_id(administration_id)

@router.delete("/{administration_id}", response_model=AdministrationResponse)
def delete_administration(administration_id: int):
    administration = db_manager.administrations.get_administration_by_id(administration_id)
    if not administration:
        raise HTTPException(status_code=404, detail="Administration not found")
    db_manager.administrations.delete_administration(administration_id)
    return administration
