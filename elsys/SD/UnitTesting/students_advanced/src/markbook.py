from random import randint


class BadSubjectGrades(Exception):

    def __init__(self, *msg):
        self.__ctx = msg


class MarkBook:

    SUBJECTS = ['Maths', 'OOP', 'C', 'OS', 'Python', 'Embedded Systems']

    def __init__(self, grades=None):
        self.__grades = grades
        if self.__grades is None:
            self.__grades = {}
            self.randomise_marks()

    def __str__(self):
        rv = "\n"
        if self.grades is not None:
            for k, v in self.grades.items():
                rv += f'\t{k} := {v}\n'
        return rv

    def __repr__(self):
        return f"MarkBook({self.grades}))"

    def randomise_marks(self):
        for subject in MarkBook.SUBJECTS:
            for _ in range(randint(0, 10)):
                rand_mark = randint(2, 6)
                self.add_mark(subject, rand_mark)

    def subject_results(self, subject):
        if subject not in self.grades:
            raise BadSubjectGrades(f"no subject '{subject}' present")
        return self.grades[subject]


    def add_mark(self, subject, mark):
        self.grades.setdefault(subject, []).append(mark)

    def get_average(self, subject):
        return sum(self.grades[subject]) / len(self.grades[subject])

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grade_dict):
        self.__grades = grade_dict





