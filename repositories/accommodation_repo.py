from models import Accommodation

class AccommodationRepository:
    def __init__(self, session):
        self.session = session

    def add_accommodation(self, student_id, room_id, date_from, date_to=None):
        accommodation = Accommodation(student_id=student_id, room_id=room_id, date_from=date_from, date_to=date_to)
        self.session.add(accommodation)
        self.session.commit()

    def get_all_accommodations(self):
        return self.session.query(Accommodation).all()

    def get_accommodation_by_id(self, accommodation_id):
        return self.session.query(Accommodation).get(accommodation_id)

    def update_accommodation(self, accommodation_id, **kwargs):
        accommodation = self.get_accommodation_by_id(accommodation_id)
        if accommodation:
            for key, value in kwargs.items():
                setattr(accommodation, key, value)
            self.session.commit()

    def delete_accommodation(self, accommodation_id):
        accommodation = self.get_accommodation_by_id(accommodation_id)
        if accommodation:
            self.session.delete(accommodation)
            self.session.commit()
