from StudentsWithExceptions import Students, DuplicateIDNumberException, InvalidNumberException
import unittest


class StudentsWithExceptionsTestCase(unittest.TestCase):

    def test_add_student(self):
        s = Students()
        s.add_student("Ivan", 2)
        s.add_student("Ivanka", 3)
        self.assertEqual(s.students, {2: "Ivan", 3: "Ivanka"})

    def test_add_student_duplication(self):
        s = Students()
        s.add_student("Ivan", 2)
        with self.assertRaises(DuplicateIDNumberException):
            s.add_student("Ivanka", 2)

    def test_lookup_student_present(self):
        s = Students()
        s.add_student("Ivan", 2)
        name = s.get_name_by_id(2)
        self.assertEqual(name, "Ivan")

    def test_lookup_student_missing(self):
        s = Students()
        with self.assertRaises(InvalidNumberException):
            name = s.get_name_by_id(2)


if __name__ == "__main__":
    unittest.main()
