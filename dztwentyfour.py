from math import sqrt


class Shape:
    def __init__(self, color):
        self.color = color


class Square(Shape):
    def __init__(self, a):
        super().__init__(color="red")
        self.a = a

    # def squar(self):
    #     print("===Квадрат===")
    #     print(f"Сторона:{self.a}")
    #     print(f"Цвет:{self.color}")
    # print(f"Площадь:{self.a * self.a}")
    # print(f"Периметр:{self.a + self.a + self.a + self.a}")
    # print((" * " * self.a + "\n") * self.a)

    def plosh(self):
        return self.a * self.a

    def perim(self):
        return self.a + self.a + self.a + self.a

    def ris(self):
        print((" * " * self.a + "\n") * self.a)

    def infor(self):
        print("===Квадрат===")
        print(f"Сторона:{self.a}")
        print(f"Цвет:{self.color}")
        print(f"Площадь:", self.plosh())
        print(f"Периметр:", self.perim())
        self.ris()


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(color="green")
        self.a = a
        self.b = b

    # def recta(self):
    #     print("===Прямоугольник===")
    #     print(f"Длина:{self.a}")
    #     print(f"Ширина:{self.b}")
    #     print(f"Цвет:{self.color}")
    #     print(f"Площадь:{self.a * self.b}")
    #     print(f"Периметр:{self.a + self.b + self.a + self.b}")
    #     print((" * " * self.b + "\n") * self.a)

    def plosh(self):
        return self.a * self.b

    def perim(self):
        return self.a + self.b + self.a + self.b

    def ris(self):
        print((" * " * self.b + "\n") * self.a)

    def infor(self):
        print("===Прямоугольник===")
        print(f"Длина:{self.a}")
        print(f"Ширина:{self.b}")
        print(f"Цвет:{self.color}")
        print(f"Площадь:", self.plosh())
        print(f"Периметр:", self.perim())
        self.ris()


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(color="yellow")
        self.a = a
        self.b = b
        self.c = c

    # def tria(self):
    #     print("===Треугольник===")
    #     print(f"Сторона a:{self.a}")
    #     print(f"Сторона b:{self.b}")
    #     print(f"Сторона c:{self.c}")
    #     print(f"Цвет:{self.color}")
    #     p = (self.a + self.b + self.c) / 2
    #     d = round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)
    #     print(f"Площадь:", d)
    #     print(f"Периметр:{(self.a + self.b + self.c) / 2}")
    #     # for i in range(self.a - 4):
    #     #     print(' ' * (self.a - i) + '*' * (2 * i - 1))

    def plosh(self):
        p = (self.a + self.b + self.c) / 2
        d = round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)
        return d

    def perim(self):
        return (self.a + self.b + self.c) / 2

    def ris(self):
        for n in range(self.a - 4):
            print(' ' * (self.a - n) + '*' * (2 * n - 1))

    def infor(self):
        print("===Треугольник===")
        print(f"Сторона a:{self.a}")
        print(f"Сторона b:{self.b}")
        print(f"Сторона c:{self.c}")
        print(f"Цвет:{self.color}")
        print(f"Площадь:", self.plosh())
        print(f"Периметр:", self.perim())
        self.ris()


# s = Square(3)
# s.squar()
# r = Rectangle(3, 7)
# r.recta()
# t = Triangle(11, 6, 6)
# t.tria()

ls = [
    Square(3),
    Rectangle(3, 7),
    Triangle(11, 6, 6)
]

for i in ls:
    i.infor()
