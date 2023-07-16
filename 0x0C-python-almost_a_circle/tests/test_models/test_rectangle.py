import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_valid_rectangle(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_valid_rectangle_with_coordinates(self):
        r = Rectangle(10, 5, 2, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_non_integer_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle("10", 5)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 5)

    def test_non_integer_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "5")

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, -5)

    def test_non_integer_x_coordinate(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 5, "2", 3)

    def test_negative_x_coordinate(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 5, -2, 3)

    def test_non_integer_y_coordinate(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 5, 2, "3")

    def test_negative_y_coordinate(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 5, 2, -3)


if __name__ == '__main__':
    unittest.main()
