class Student(object):
    """ Simple Student class"""

    def __init__(self, name, surname, attendance = 0, scores = []):
        self.name = name
        self.surname = surname
        self.attendance = attendance
        self.scores = scores

    def insert_score(self, score):
        self.scores.append(score)

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def total_attendance(self)
        return self.attendance
