class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b


class Right_Triangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def triangle(self):
        return round((self.a ** 2 + self.b ** 2) ** 0.5, 2)

    def plosh(self):
        return round(self.a * self.b) / 2

    def summ(self):
        return self.a + self.b

    def proizv(self):
        return self.a * self.b

    def info(self):
        print(f'Треугольник ABC:'
              f'\nГипотенуза: {self.triangle()}'
              f'\nПрямоугольный треугольник: ({self.a}, {self.b}, {self.triangle()})'
              f'\nПлощадь: {self.plosh()}'
              f'\n'
              f'\nСумма: {self.summ()}'
              f'\nПроизводная: {self.proizv()}')


ret = Right_Triangle(5, 8)
ret.info()
print()
ret.set_a(10)
ret.triangle()
ret.info()
print()
ret.set_b(20)
ret.triangle()
ret.info()
