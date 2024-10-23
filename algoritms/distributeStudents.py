from sqlalchemy.orm import Session
from models.student import Student, GenderEnum
from models.room import Room, RoomTypeEnum
from models.accommodation import Accommodation



def distribute_students(session: Session):
    # Получаем всех студентов и сортируем по курсу и количеству нарушений
    students = session.query(Student).order_by(Student.course, Student.violations).all()

    # Получаем все комнаты
    rooms = session.query(Room).all()

    accommodations = []

    for student in students:
        # Ищем подходящую комнату
        suitable_room = None
        for room in rooms:
            if room.room_type == RoomTypeEnum.male and student.gender == GenderEnum.male and room.occupied_beds < room.bed_count:
                suitable_room = room
                break
            elif room.room_type == RoomTypeEnum.female and student.gender == GenderEnum.female and room.occupied_beds < room.bed_count:
                suitable_room = room
                break

        if suitable_room:
            # Создаем запись о размещении
            accommodation = Accommodation(student_id=student.id, room_id=suitable_room.id)
            session.add(accommodation)
            accommodations.append(accommodation)

            # Обновляем количество занятых мест в комнате
            suitable_room.occupied_beds += 1
            session.commit()
        else:
            print(f"No suitable room found for student {student.id}")

    return accommodations