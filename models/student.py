
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    birth_date = Column(Date)
    contact_info = Column(String, unique=True, index=True)
    course = Column(Integer)
    is_non_local = Column(Boolean, default=False)
    hashed_password = Column(String)  # New field for hashed password

    # Relationship with violations
    violations = relationship('Violation', back_populates='student')

    # Relationship with accommodations
    accommodations = relationship('Accommodation', back_populates='student')

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.first_name} {self.last_name}, course={self.course})>"