class Student(object):
    """ Simple Student class"""

    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def insert_score(self, score):
        self.scores.append(score)

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def total_attendance(self)
        return self.attendance
