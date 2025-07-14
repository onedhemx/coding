from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Вычисление площади фигуры"""
        pass

    @abstractmethod
    def perimeter(self):
        """Вычисление периметра фигуры"""
        pass

    def info(self):
        """Вывод информации о фигуре"""
        print(f"Фигура: {self.__class__.__name__}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
