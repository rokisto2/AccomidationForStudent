from models import Administration

class AdministrationRepository:
    def __init__(self, session):
        self.session = session

    def add_administration(self, first_name, last_name, dormitory_id, contributions=0):
        admin = Administration(first_name=first_name, last_name=last_name, dormitory_id=dormitory_id, contributions=contributions)
        self.session.add(admin)
        self.session.commit()

    def get_all_administrators(self):
        return self.session.query(Administration).all()

    def get_administration_by_id(self, admin_id):
        return self.session.query(Administration).get(admin_id)

    def update_administration(self, admin_id, **kwargs):
        admin = self.get_administration_by_id(admin_id)
        if admin:
            for key, value in kwargs.items():
                setattr(admin, key, value)
            self.session.commit()

    def delete_administration(self, admin_id):
        admin = self.get_administration_by_id(admin_id)
        if admin:
            self.session.delete(admin)
            self.session.commit()
