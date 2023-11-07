class Clock:
    __Day = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__Day

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock:")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec == other.sec
        # if self.sec == other.sec:
        #     return True
        # return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "hour":
            return (self.sec // 3600) % 24
        elif item == "min":
            return (self.sec // 60) % 60
        elif item == "sec":
            return self.sec % 60

        return "Не верный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if not isinstance(value, int):
            raise ValueError("Значение должен быть целым числом")
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        if key == "hour":
            self.sec = s + 60 * m + value * 3600
        elif key == "min":
            self.sec = s + 60 * value + h * 3600
        elif key == "sec":
            self.sec = value + 60 * m + h * 3600

    def __it__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec < other.sec

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec <= other.sec

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec >= other.sec


x1 = Clock(400)
print(x1.get_format_time())
# x1["hour"] = 9
# x1["min"] = 61
# x1["sec"] = 32
# print(x1["hour"], x1["min"], x1["sec"])
# print(x1.get_format_time())
x2 = Clock(400)
print(x2.get_format_time())
print()
x1 += x2
print("x1 += x2", x1.get_format_time())
x1 -= x2
print("x1 -= x2", x1.get_format_time())
x1 *= x2
print("x1 *= x2", x1.get_format_time())
x1 //= x2
print("x1 //= x2", x1.get_format_time())
x1 %= x2
print("x1 %= x2", x1.get_format_time())
print()
x3 = x1 + x2
print("x1+x2:", x3.get_format_time())

x4 = x1 - x2
print("x1-x2:", x4.get_format_time())

x5 = x1 * x2
print("x1*x2:", x5.get_format_time())

x7 = x1 // x2
print("x1//x2:", x7.get_format_time())

x8 = x1 % x2
print("x1%x2:", x8.get_format_time())

# Проверка

# if x1 == x2:
#     print("Время одинаково")
# else:
#     print("Время разное")

# if x1 != x2:
#     print("Время разное")
# else:
#     print("Время одинаково")

# if x1 <= x2:
#     print("Правильно")
# else:
#     print("Введите другое число х1")

# if x1 < x2:
#     print("Не правильно")
# else:
#     print("Введите другое число х1")

# if x1 > x2:
#     print("Правильно")
# else:
#     print("Введите другое число х1")

# if x1 >= x2:
#     print("Правильно")
# else:
#     print("Введите другое число х1")
