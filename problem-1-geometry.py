import math
import unittest

# Создаём класс, от которого будут наследоваться все остальные фигуры
class Shape:
    def area(self) -> float:
        """Метод для вычисления площади. Должен быть переопределен в дочерних классах"""
        pass

# Класс круга, который наследуется от родительского Shape и для создания требует параметр - радиус
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float: # Метод вычисления площади переопределен по формуле площади созданной фигуры. У круга Pi * r ** 2
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if a + b <= c or a + c <= b or b + c <= a: # Проверка на неравенство треугольника. Сумма двух сторон треугольника всегда должна быть большей третей. Если это не выполняется - значит такой треугольник создать невозможно
            raise ValueError("Triangle with these side lengths cannot be created")
        else:
            self.a = a
            self.b = b
            self.c = c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def is_right_angled(self) -> bool:
        a, b, c = sorted([self.a, self.b, self.c])
        return a ** 2 + b ** 2 == c ** 2


# Класс любого ПРАВИЛЬНОГО многоугольника. Для создания необходимо количество сторон и их длина
# В задании указан критерий "Лёгкость добавления других фигур", не совсем понял интерпретацию. Лёгкость добавления в плане создания новых классов новых фигур? В таком случае для создания новой фигуры, нужно лишь задать ей необходимые параметры для вычисления площади и добавить метод area с формулой вычисления площади
# Или же критерий можно интерпретировать как добавления новых фигур с помощью одного класса. Я так и понял эту задачу и реализовал класс Polygon
class Polygon(Shape):
    def __init__(self, length: int, number_of_sides: int):
        if number_of_sides < 3:
            raise ValueError("Polygon cannot have less than 3 sides.")
        else:
            self.length = length
            self.number_of_sides = number_of_sides

    def area(self) -> float:
        # Формула правильного многоугольника (n * a ** 2) / (4 * tg * (Pi / n))
        first = self.number_of_sides * self.length ** 2
        second = 4 * math.tan((math.pi / self.number_of_sides))
        return first / second


# ------

# Функция принимает фигуру как класс, затем вызывает её заранее определенный метод вычисления площади
def calculate_area(shape: Shape) -> float:  
    return shape.area()

# ------
 
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



if __name__ == '__main__':
    unittest.main()

tri = Triangle(1, 2, 3)
poly = Polygon(
    number_of_sides=6,
    length=10
)
print(poly.area()) # ~259.8076211353316
