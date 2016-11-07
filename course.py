class Course(object):
    def __init__(self, name):
        self.name = name
        self.student_ids = []

    def add_student(self, student_id):
        self.student_ids.append(student_id)
