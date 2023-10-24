import math


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, val):
        if Rectangle.check_value(val):
            self.__length = val
        else:
            print("Не верный тип данных")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if Rectangle.check_value(val):
            self.__width = val
        else:
            print("Не верный тип данных")

    @staticmethod
    def check_value(s):
        if isinstance(s, (int, float)):
            return True
        return False

    def square(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length + self.__width) * 2

    def hypotenuse(self):
        s = (self.__length ** 2 + self.__width ** 2) ** 0.5
        return round(s, 2)

    def print_rec(self):
        return ("*" * self.__width + "\n") * self.__length


p1 = Rectangle(3, 9)
print("Длина прямоугольника:", p1.length)
print("Ширина прямоугольника:", p1.width)
p1.length = "2"
p1.width = "7"
print("Длина прямоугольника:", p1.length)
print("Ширина прямоугольника:", p1.width)
print(f"Площадь прямоугольника:", p1.square())
print(f"Гипотенуза прямоугольника:", p1.hypotenuse())
print("Периметр прямоугольник:", p1.perimeter())
print(p1.print_rec())
