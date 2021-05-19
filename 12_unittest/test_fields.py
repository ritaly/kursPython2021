import unittest
from fields import rectangle, triangle, trapezoid


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 2
        self.b = 10
        self.h = 2

    def test_rectangle_with_correct_values(self):
        result = rectangle(self.a, self.b)
        self.assertEqual(result, 20)

    # def test_rectangle_with_incorrect_values(self):
    #     self.assertRaises(ValueError, rectangle, self.a, '***')
    def test_rectangle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            rectangle('***', self.b)

    def test_triangle_with_correct_values(self):
        result = triangle(self.a, self.b)
        self.assertEqual(result, 10)

    def test_trapezoid_with_correct_values(self):
        result = trapezoid(self.a, self.b, self.h)
        self.assertEqual(result, 12)

    def tearDown(self):
        del self.a
        del self.b


if __name__ == '__main__':
    unittest.main()
