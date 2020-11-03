from src.student import Student
import unittest


class StudentTestCase(unittest.TestCase):

    def test_init(self):
        st = Student("test name")
        flag = st is not None and st.id is not None and st.computer is not None and st.marks is not None
        self.assertTrue(flag)
