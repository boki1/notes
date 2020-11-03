from CustomStack import CustomStack
import unittest


class CustomStackTestCase(unittest.TestCase):

    def test_stack_push(self):
        s = CustomStack()
        s.push("New element")
        self.assertEqual(s.elements, ["New element"])

    def test_stack_size_after_push(self):
        s = CustomStack()
        s.push("New element")
        self.assertEqual(s.size(), 1)

    def test_stack_pop_empty(self):
        s = CustomStack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_stack_size_after_pop(self):
        s = CustomStack()
        s.push("a")
        s.push("b")
        s.push("c")
        el = s.pop()
        self.assertEqual(s.size(), 2)

    def test_stack_pop(self):
        s = CustomStack()
        s.push("a")
        s.push("b")
        s.push("c")
        el = s.pop()
        self.assertEqual(s.elements, ["a", "b"])


if __name__ == "__main__":
    unittest.main()
