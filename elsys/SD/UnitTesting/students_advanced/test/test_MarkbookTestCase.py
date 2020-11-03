from src.markbook import MarkBook, BadSubjectGrades
import unittest


class MarkbookTestCase(unittest.TestCase):

    def test_adding(self):
        m = MarkBook(grades={})
        m.add_mark("Literature", 3)
        m.add_mark("Literature", 3)
        m.add_mark("Literature", 4)
        self.assertEqual(m.grades, {"Literature": [3, 3, 4]})

    def test_filtered_displaying_bad_call(self):
        m = MarkBook(grades={})
        m.add_mark("Literature", 3)
        m.add_mark("Literature", 3)
        m.add_mark("Literature", 4)
        with self.assertRaises(BadSubjectGrades):
            m.subject_results("Maths")

    def test_filtered_displaying(self):
        m = MarkBook(grades={})
        m.add_mark("Literature", 3)
        m.add_mark("Maths", 5)
        m.add_mark("Literature", 4)
        lst = m.subject_results("Maths")
        self.assertEqual(lst, [5,])

