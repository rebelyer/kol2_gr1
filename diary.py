from student import Student
from datetime import date
import yaml


class Diary(object):
    """ Poprawa:
            * maksymalnie 3 klasy
            * zapis i wczytywanie do pliku
            * kazda z klas maksymalnie 5 funkcji
            * kazda z funkcji 4 linijki nie liczac nazwy funkcji i return (czyli razem 6 xd)
    """
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        assert isinstance(student, Student)
        self.students[student.first_name + " " + student.surname] = student

    @property
    def average_score(self):
        sum_scores, scores_number = 0, 0
        for student in self.students.values():
            sum_scores += sum(student.all_marks)
            scores_number += len(student.all_marks)
        return 0 if scores_number == 0 else float(sum_scores) / scores_number

    def dump_to_file(self, file_name="diary.yml"):
        with open(file_name, 'w') as outfile:
            yaml.dump(self.students, outfile, default_flow_style=False)

    def load_from_file(self, file_name="diary.yml"):
        with open(file_name, 'r') as file:
            self.students = yaml.load(file)


if __name__ == "__main__":
    diary = Diary()
    diary.add_student(Student("Wojciech", "Zygmuntowicz"))
    diary.add_student(Student("Kamil", "Malenczuk"))
    diary.students["Wojciech Zygmuntowicz"].add_to_course("Fizyka")
    diary.students["Wojciech Zygmuntowicz"].add_to_course("Matematyka")
    diary.students["Wojciech Zygmuntowicz"].mark_as_present("Fizyka", date(2016, 3, 14))
    diary.students["Wojciech Zygmuntowicz"].mark_as_present("Fizyka", date(2016, 3, 16))
    diary.students["Wojciech Zygmuntowicz"].give_a_mark("Fizyka", date(2016, 3, 14), 5)
    diary.students["Wojciech Zygmuntowicz"].give_a_mark("Fizyka", date(2016, 3, 14), 4)
    print diary.students["Wojciech Zygmuntowicz"].average_score_in_course("Fizyka")
    print diary.average_score
    diary.dump_to_file()