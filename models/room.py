from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .base import Base
import enum

class RoomTypeEnum(enum.Enum):
    male = "male"
    female = "female"
    family = "family"


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    dormitory_id = Column(Integer, ForeignKey('dormitories.id'), nullable=False)
    room_number = Column(String(10), nullable=False)
    room_type = Column(Enum(RoomTypeEnum), nullable=False)
    bed_count = Column(Integer, nullable=False)
    occupied_beds = Column(Integer, default=0)

    # Relationship with dormitory
    dormitory = relationship('Dormitory', back_populates='rooms')

    # Relationship with accommodations
    accommodations = relationship('Accommodation', back_populates='room')

    def __repr__(self):
        return f"<Room(id={self.id}, dormitory={self.dormitory.name}, room_number={self.room_number}, bed_count={self.bed_count})>"