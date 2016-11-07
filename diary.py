import student
import course

class Diary(object):
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []

    def add_course(self, course_name):
        self.courses.append(Course(course_name))

    def add_student(self, student_first_name, student_last_name):
        self.students.append(Student(student_first_name, student_last_name))



