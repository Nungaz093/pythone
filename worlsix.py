import math

print("Выберите номер фигуры: 1 - Прямоугольник, 2 - Треугольник, 3 - Круг")
number = int(input("Номер фигуры: "))


def figura(z):
    s = 0
    if z == 1:
        a = int(input("Длина прямоугольник: "))
        b = int(input("Ширинра прямоугольник: "))
        s = a * b
        print(s)
    elif z == 2:
        a = int(input("Введите сторону a = "))
        b = int(input("Введите сторону b = "))
        c = int(input("Введите сторону c = "))
        p = (a + b + c) / 2
        s = math.sqrt((p * (p - a) * (p - b) * (p - c)))
        print(s)
    elif z == 3:
        r = int(input("Введите радиус r = "))
        s = math.pi * (r ** 2)
        print(s)
    else:
        print(number, "Нет такой цифры и фигуры")


figura(number)
