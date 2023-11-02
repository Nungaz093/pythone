class Figure:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Rectangle(Figure):
    def __init__(self, x, y, color):
        self.verify(x)
        self.verify(y)
        self.__x = x
        self.__y = y
        super().__init__(color)

    def square(self):
        return self.__x * self.__y

    @staticmethod
    def verify(val):
        if val < 0:
            raise ValueError('Переменная не должна быть отрицательной')

    def get_info(self):
        print(f'Высота: {self.__x}'
              f'\nШирина: {self.__y}'
              f'\nЦвет: {self.get_color()}'
              f'\nПлощадь: {self.square()}')


first = Rectangle(6, 7, 'red')
first.set_color('black')
first.get_info()
second = Rectangle(5, -6, 'green')
