from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class DeaneryStaff(Base):
    __tablename__ = 'deanery_staff'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    contact_info = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<DeaneryStaff(id={self.id}, name={self.first_name} {self.last_name}, department={self.department}, position={self.position})>"