from sqlalchemy import Column, Integer, String, Date, Boolean, Enum
from sqlalchemy.orm import relationship
from .base import Base
import enum

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    birth_date = Column(Date)
    contact_info = Column(String(100), unique=True, index=True)
    course = Column(Integer)
    is_non_local = Column(Boolean, default=False)
    hashed_password = Column(String(100))  # New field for hashed password
    gender = Column(Enum(GenderEnum), nullable=False)  # New field for gender

    # Relationship with violations
    violations = relationship('Violation', back_populates='student')

    # Relationship with accommodations
    accommodations = relationship('Accommodation', back_populates='student')

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.first_name} {self.last_name}, course={self.course})>"