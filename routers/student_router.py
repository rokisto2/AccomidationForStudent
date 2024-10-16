from datetime import date

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db_manager_factory import get_db_manager

router = APIRouter()

db_manager = get_db_manager()


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: str
    contact_info: str
    course: int
    is_non_local: bool


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: date  # Делаем его строкой, чтобы избежать ошибок сериализации
    contact_info: str
    course: int
    is_non_local: bool

    class Config:
        orm_mode = True
        json_encoders = {
            date: lambda v: v.isoformat()  # Преобразуем дату в строку формата 'YYYY-MM-DD'
        }

@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate):
    db_manager.students.add_student(**student.dict())
    new_student = db_manager.students.get_all_students()[-1]
    return new_student


@router.get("/", response_model=list[StudentResponse])
def read_students():

    return db_manager.students.get_all_students()
