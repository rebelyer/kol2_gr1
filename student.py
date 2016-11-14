from datetime import date


class Student(object):
    """ Simple Student class"""

    def __init__(self, first_name, surname):
        assert isinstance(first_name, str)
        assert isinstance(surname, str)
        self.first_name, self.surname = first_name, surname
        self.courses = {}

    def add_to_course(self, course):
        assert isinstance(course, str)
        self.courses[course] = {}

    def mark_as_present(self, course, day):
        assert isinstance(course, str)
        assert isinstance(day, date)
        self.courses[course][day] = []

    def give_a_mark(self, course, day, grade):
        assert isinstance(course, str)
        assert isinstance(day, date)
        assert isinstance(grade, int)
        self.courses[course][day].append(grade)

    def average_score_in_course(self, course):
        assert isinstance(course, str)
        marks = [mark for sub_list in self.courses[course].values() for mark in sub_list]
        return 0 if len(marks) == 0 else float(sum(marks)) / len(marks)

    @property
    def all_marks(self):
        list_of_lists_of_marks = [mark.values() for mark in self.courses.values()]
        list_of_lists = [val for sub_list in list_of_lists_of_marks for val in sub_list]
        return [mark for sub_list in list_of_lists for mark in sub_list]
