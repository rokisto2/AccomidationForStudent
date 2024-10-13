from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    dormitory_id = Column(Integer, ForeignKey('dormitories.id'), nullable=False)
    room_number = Column(String(10), nullable=False)
    room_type = Column(String(10), nullable=False)  # Мужская, женская, семейная
    bed_count = Column(Integer, nullable=False)  # Количество кроватей
    occupied_beds = Column(Integer, default=0)  # Занятые кровати

    # Связь с общежитием
    dormitory = relationship('Dormitory', back_populates='rooms')

    # Связь с заселениями
    accommodations = relationship('Accommodation', back_populates='room')

    def __repr__(self):
        return f"<Room(id={self.id}, dormitory={self.dormitory.name}, room_number={self.room_number}, bed_count={self.bed_count})>"
