class StudentsException(Exception):

    def __init__(self, *msg):
        self.__cts = msg


class DuplicateIDNumberException(StudentsException):

    def __init__(self, *msg):
        super().__init__(*msg)


class InvalidNumberException(StudentsException):

    def __init__(self, *msg):
        super().__init__(*msg)


class Students:

    def __init__(self):
        self.students = {}

    def add_student(self, name, number):
        if number in self.students:
            raise DuplicateIDNumberException(f"failed adding '{name}' with id='{number}'")
        self.students[number] = name

    def get_name_by_id(self, number):
        if number not in self.students:
            raise InvalidNumberException
        return self.students[number]

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, s):
        self.__students = s


