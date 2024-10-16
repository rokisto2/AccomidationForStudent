from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Administration(Base):
    __tablename__ = 'administration'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    contact_info = Column(String, unique=True, index=True)
    dormitory_id = Column(Integer, ForeignKey('dormitories.id'), nullable=False)
    contributions = Column(Integer, default=0)  # Contributions
    hashed_password = Column(String, nullable=False)  # New field for password

    # Relationship with dormitory
    dormitory = relationship('Dormitory')

    def __repr__(self):
        return f"<Administration(id={self.id}, name={self.first_name} {self.last_name}, contributions={self.contributions})>"
