import math
import unittest


class Shape:
    def area(self) -> float:
        """Метод для вычисления площади. Должен быть переопределен в дочерних классах"""
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def is_right_angled(self) -> bool:
        a, b, c = sorted([self.a, self.b, self.c])
        return a ** 2 + b ** 2 == c ** 2


def calculate_area(shape: Shape) -> float:
    return shape.area()


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_is_right_angled(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)


if __name__ == '__main__':
    unittest.main()

tri = Triangle(1, 2, 3)
