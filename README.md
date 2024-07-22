# MindBox-test-problems-geometry-and-pyspark

Тестовое задание:

1. Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:
- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time
- Проверку на то, является ли треугольник прямоугольным

С моей стороны выполнено:
- Добавлены юнит-тесты
- Фигуры можно добавить просто создав класс и написав функцию вычисления площади для конкретной фигуры
- Реализован класс по созданию любого прямого многоугольника
- Реализована проверка на то, является ли треугольник прямоугольным треугольником через формулу Пифагора


2. В PySpark приложении датафреймами(pyspark.sql.DataFrame) заданы продукты, категории и их связи. Каждому продукту может соответствовать несколько категорий или ни одной. А каждой категории может соответствовать несколько продуктов или ни одного. Напишите метод на PySpark, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий. Приведите пример работы вашего метода в Jupyter ноутбуке.

