from models import Student

class StudentRepository:
    def __init__(self, session):
        self.session = session

    def add_student(self, first_name, last_name, birth_date, contact_info, course, is_non_local):
        student = Student(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            contact_info=contact_info,
            course=course,
            is_non_local=is_non_local
        )
        self.session.add(student)
        self.session.commit()

    def get_all_students(self):
        return self.session.query(Student).all()

    def get_student_by_id(self, student_id):
        return self.session.query(Student).get(student_id)

    def update_student(self, student_id, **kwargs):
        student = self.get_student_by_id(student_id)
        if student:
            for key, value in kwargs.items():
                setattr(student, key, value)
            self.session.commit()

    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)
        if student:
            self.session.delete(student)
            self.session.commit()
