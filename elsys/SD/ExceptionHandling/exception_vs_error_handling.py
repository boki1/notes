class InvalidNumberException(BaseException):

    def __init__(self, cntx=None):
        self.failed_id_num = cntx


class StudentClass:

    def __init__(self, dct=None):
        if dct is None:
            dct = {}
        self.students = dct

    def by_name(self, id_number):
        if id_number in self.students:
            return self.students[id_number]
        else:
            raise InvalidNumberException

    def by_name_errh(self, id_number):
        if id_number in self.students:
            return self.students[id_number]
        else:
            return ""


def main():
    xi_a = StudentClass({1: "Perrin Aibara", 2: "Lan Mandragoran",
                         5: "Moarein Sedai", 7: "Falsedragon Logain"})

    print("---------------")
    print("Exception handling")
    print("---------------")

    for id_num in range(10):
        try:
            st = xi_a.by_name(id_num)
        except InvalidNumberException:
            print(f"Student with Id {id_num} is not found.")
        else:
            print(f"Student with Id {id_num} is called {st}")

    print("---------------")
    print("Error handling")
    print("---------------")

    for id_num in range(10):
        st = xi_a.by_name_errh(id_num)
        if st == "":
            print(f"Student with Id {id_num} is not found.")
        else:
            print(f"Student with Id {id_num} is called {st}")



if __name__ == "__main__":
    main()
