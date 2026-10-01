import unittest

from week02.Student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student('', 1, 100)

    def test_updateMark(self):
        self.student.update_mark(72)
        self.assertEqual(self.student.mark, 72)
        self.student.update_mark(0)
        self.assertEqual(self.student.mark, 0)
        original_mark = self.student.mark
        self.student.update_mark(120)
        self.assertEqual(self.student.mark, original_mark)
        self.student.update_mark(-20)
        self.assertEqual(self.student.mark, original_mark)

if __name__ == '__main__':
    unittest.main()
