#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class Diary(object):

    def __init__(self, students={}):
        # FIXME make assertion for students class
        assert True
        self.students = students

    def add_student(self, student, student_id):
        try:
            self.students[student_id]
        except KeyError:
            self.students[student_id] = student
        else:
            raise RuntimeError("There is already student with this id")

    def remove_student(self, student_id):
        try:
            self.students.pop(student_id)
        except:
            raise RuntimeError("There is no student with that id")

    def find_student(self, student_id):
        return self.students[student_id]

    def total_average_score(self):
        return sum( [for student.average_score in self.students] )

    def average_score_in_class(self, a):
        return True

    def total_attendance_of_student(self, student_id):
        student = self.find_student(student_id)
        return student.total_attendance
