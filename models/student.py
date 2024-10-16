from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    contact_info = Column(String(100))
    course = Column(Integer, nullable=False)
    is_non_local = Column(Boolean, nullable=False)  # True for non-local students
    hashed_password = Column(String, nullable=False)  # New field for password

    # Relationship with violations
    violations = relationship('Violation', back_populates='student')

    # Relationship with accommodations
    accommodations = relationship('Accommodation', back_populates='student')

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.first_name} {self.last_name}, course={self.course})>"