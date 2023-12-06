# name = "User"
# print("Hello,", name)
# age = 20
# print(age)
# print(type(age))
# age = "hello"
# print(age)
# print(type(age))
# import copy
import re

# a = 4
# print("a =", id(a))
# b = 5
# print("b =", id(b))
# a = b
# print(a)

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "hello", 9.21
# print(a, b, c)

# PI = 3.14
# print(PI)

# name = "Игорь"
# age = 36
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")

# a = 5
# b = 7
# print("a:", a)
# print("b:", b)
# temp = a
# a = b
# b = temp
# print("a:", a)
# print("b:", b)

# print(5/3)
# print(5//3)


# Функция явного преоброзования типов
# int


# s1 = "2"
# s2 = 5
# print(int(s1) + s2)
# print(s1 + str(s2))

# print(5566345323445)
# print(type(5.566345323445))


# a, b, c = 5, 7, 3
# sum1 = a + b + c
# pr = a * b * c
# sr = sum1 / 3
# print('сумма: ', sum1, '\nпроизведение: ', pr, '\nсреднее: ', sr)

# number = 6 + 4 * 5 ** 2 + 7
# #              2    1   3
# print(number)

# num = 10
# num += 5  # num = num + 5
# print(num)
# num -= 3
# print(num)  # 12

# num = 9753
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# c = num % 10
# print("c:", c)
# num = num // 10
# d = num % 10
# print("d:", d)
# print(a * 1000 + b * 100 + c * 10 + d * 1)

# num = 4321
# print("Исходное число:", num)
# res = num % 10 * 1000
# num = num // 10
# res += num % 10 * 100
# num = num // 10
# res += num % 10 * 10
# num = num // 10
# res += num % 10
# print(res)

# print(int(3.45677896))
# print(round(3.45677896, 4))

# a = '5.2'
# b = 10
# print(float(a) + b)

# a = 1
# b = 2
# print("a:", a, "\nb:", b)

# name = "Виктор"
# age = 21
# print("Меня зовут", name,  ". Мне ", age, "лет.",)
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name,  ". Мне ", age, " лет.", sep="", end="\n\n")
# print("Привет")

# name = input("Введите " + "имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = int(num) ** int(power)
# print(res)


# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)


# print(bool("python"))
# print(bool(""))  # False
# print(bool(" "))
# print(bool("9"))
# print(bool("0"))  # False
# print(bool(False))  # False
# print(bool(None))  # False


# test = None
# print(test)
# test = 5
# print(test)

# print(2 + 5 == 7)

# print(2 < 4 < 9)  # True True
# print(2 * 5 > 7 >= 4 + 3)  # 10 > 7 >= 7 True True
#
# print(3 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False


# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True => true
# print(5 - 3 == 3 and 1 + 3 == 4)  # False and True => False
# print(5 - 3 == 2 and 1 + 3 == 5)  # True and False => False
# print(5 - 3 == 3 and 1 + 3 == 5)  # False and False => False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True and True => true
# print(5 - 3 == 3 or 1 + 3 == 4)  # False and True => true
# print(5 - 3 == 2 or 1 + 3 == 5)  # True and False => true
# print(5 - 3 == 3 or 1 + 3 == 5)  # False and False => False

# print(not 9 - 5)  # 4(True) => False
# print(not 9 - 9)  # 0(False) => True


# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возвраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 15
# b = 50
# # if a > b:
# #     print("a > b")
# # elif a < b:
# #     print("b > a")
# # else:
# #     print("a == b")
#
# if a > b:
#     print("a > b")
# if a < b:
#     print("b > a")
# if a == b:
#     print("a == b")


# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
# if a == b == c:
#     print("Треугольник равностороний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедреный")
# else:
#     print("Треугольник разностороний")

# day = int(input("Введите дни недели цифрой: "))
# if 1 <= day <= 5: #  (day >= 1) and (day <= 5):
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день -", end=" ")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует")

# num = int(input("Введите дни недели цифрой: "))
# if num == 1 or num == 2 or num == 12:
#     print("Зима")
# elif 3 <= num <=5:
#     print("Весна")
# elif 6 <= num <= 8:
#     print("Лето")
# elif 9 <= num <= 11:
#     print("Осень")
# else:
#     print("Не верный номер")

# n = int(input("Введите количество ворон от 0 до 9: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("Ворона")
#     elif 2 <= n <= 4:
#         print("Вороны")
#     else:
#         print("Ворон")
# else:
#     print("Ошибка данных")

# day = 'Понедельник'
# time = 12
#
# match day:
#     case 'Понедельник' | 'Вторник' | 'Среда' | 'Четверг' |'Пятница' if 9 <= time <=16:
#         print("Рабочий день")
#     case 'Суббота'|'Воскресенье':
#         print("Выходной")
#     case _:
#         print("Такого дня не существует или не рабочее время")


# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 40, 50
# print("a == b" if a == b else "a > b" if a > b else "b > a")


# a, b = 20, 10
# print("На ноль делить нельзя" if b == 0 else a / b)


# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что то пошло не так")

#
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# try:  # попытаться
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):  # исключение
#     print("Нельзя вводить строки, или нельзя делить на ноль ")
# else:  # когда в блоке try не возникло исключений
#     print("Все норм. Вы ввели", n, "и", m)
# finally:  # вы полнится в любом случае
#     print("Конец программы")

# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
#
# try:
#     a = int(a)  # 'l'
#     b = int(b)  # '8'
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)


# Циклы

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 10:
#     b = i*2
#     print(b)
#     i += 1

# n = int(input("Укажите кол-во символов: "))
# i = 0
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("введите число: "))
# print('*' * a)

# print('*' * int(input("введите число: ")))

# a = int(input("Введем начало диапозона: "))
# b = int(input("Введем конец диапозона: "))
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a  # res = res + a => 0 + 1
#     a += 1
# print(res)

# n = input("Введите число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите число: ")
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n <= 0:
#         break

# res = 1
# while True:
#     numb = int(input('Введите число: '))
#     if numb == 0:
#         break
#     res *= numb
# print("Результат:", res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутрений цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#         print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
# print()
# i += 1


# for i in 'Hello':
#     print(i)

# for color in 'red', 'blue', 'black':
#     print(color)

# print(range(8))
#   # range(start,stop,step)
#            0,     8,  1


# for i in range(8):
#     print(i, end=" ")
#
# print()
# j = 0
# while j < 8:
#     print(j, end=" ")
#     j += 1


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
# else:
#     print('done')


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("\t--")
#         # for k in range(2):
#         #     print("**")

# p = int(input("Введите длину прямоугольника"))
# d = int(input("Введите высоту прямоугольника"))
# for i in range(d):
#     print("*" * p)


# p = int(input("Введите длину прямоугольника: "))
# d = int(input("Введите высоту прямоугольника: "))
# for i in range(d):
#     for j in range(p):
#         if i == 0 or i == d - 1 or j == 0 or j == p - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# a = [b * 2 for b in "Banana"]
# print(a)
#
# ty = [i for i in range(36) if i % 2 == 0]
# print(ty)


# Список

# nums = [8, 3, 9, 4, 1]
# #       0  1  2  3  4
# #      -5 -4 -3 -2 -1
# # print(nums)
# # print(type(nums))
# # print(nums[0])
# # print(nums[4])
# # print(nums[-1])
# # nums[3] = 255
# # nums[1] += 255
# print(nums)
# print(len(nums))

# s = []
# print(s)
# print(type(s))
#
# s1 = list("Hello")
# print(s1)
# print(type(s1))

# n = list(range(2, 10))
# print(n)
# n = int(input("das: "))
# a = [ "*" for i in range(n)]
# print(a)
#
#
# s = [ v * 3 for v in "list"]
# print(s)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)


# p = [0] * int(input("Введите кол-во элементов списка: "))
# print(p)
# for i in range(len(p)):
#     p[i] = input("==> ")
# print(p)

# a = [input("==> ") for i in range(int(input("n = ")))]
# print(a)

# a = [4, 8, 9, 5, 3]
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
# for i in a:
#     print(i, end=" ")

# res = 0
# a = [input("--> ") for i in range(int(input("Ввод чисел: ")))]
# for i in range(len(a)):
#     if a[i] < 0:
#         res += a[i]
# print(res)


# res = 0
# n = list(range(21, 41))
# count = 0
# nechet = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         nechet += n[i]
# print(count, nechet)


# a = [7, 9, 2, 1, 17]
# a[0], a[1] = a[1], a[0]
# print(a)

# Срезы

# s = [5, 9, 3, 7, 1, 8]
# # имя списка[start:stop:step]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::-1])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1:6:2])
# print(s[0:1])
# print(s[6:])
# print(s[3:4])
# print(s[4:8])
# print(s[-3:1:-1])
# print(s[2:5])


# s = list(range(1, 8))
# print(s)
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[9:10] = [30]
# print(s)


# Методы списков
# s = [1, 20, 0, 0, 0, 4, 5, 6, 7, 30]
# print(s)
# s.append(99)  # добавляет 1-н элемент в конец списка
# print(s)
# s.extend([5, 4, 3])  # добовл список из нескольких элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 100)  # добовл элемент (2-й парраметр) списка  в заданый индекс(1-й парраметр)
# print(s)
# s.insert(9, 300)
# print(s)
# s.insert(20, 600)
# print(s)


# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s)

# s = []
# n = int(input("Введите число кратное 3"))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 3 == 0:
#         s.insert(0, x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)


# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)


# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)


# s = [11, 1, 22, 2, 33, 3, 4, 5]
# # s[3:] = []
# # del s[2]
# print(s)
# # n = 11
# # if n in s:
# #     s.remove(n)  # удалит элемент из списка по значению
# # last = s.pop(-3)  # удаление по индексу заданному в круглых скобках, если индекс не передан то последжний элем из
# списка удаляет


# # s.clear()
# # print(last)
# print(s)

# a = [int(input("==>")) for i in range(int(input("n = ")))]
# k = int(input("Введите мндекс: "))
# a.pop(k)
# print(a)


# s = [11, 3, 1, 22, 3, 2, 33, 3, 4, 5]
# # num = s.count(23)  # подсчет кол-во заданых значений в списке
# # print(s)
# print(s)
# ind = s.index(3, 5)  # возвращяет индекс первого элементаБ можно передать параметры start и stop
# print(ind)

# s = [11, 3, 1]
# b = s
# print("s = ", s)
# print("b = ", b)
# b.append(120)
# s.append(30)
# print("s = ", s)
# print("b = ", b)

# s = [11, 3, 1, 22, 3, 2, 33, 3, 4, 5]
# # # s.reverse()  # Представляет элем в обратном порядке
# s.sort(reverse=True)  # Сортировка по возрастанию, revers=True по убыв
# # print(s)
# n = sorted(s, reverse=True)
# print(s)
# print(n)
# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s.sort(key=len, reverse=True)
# print(s)

# Генерация случайных данных

# import random

# print(random.random())
# print(random.randint(1, 9))
# print(random.randrange(1, 9, 2))

# from random import randint, randrange
#
# print(randint(1, 9))
# print(randrange(1, 9, 2))

# from random import *
#
# print(randint(1, 9))
# print(randrange(1, 9, 2))

# import random as r

# print(r.randint(1, 9))
# print(r.randrange(1, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))


# city = ['Москва', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
# print(r.choices(city, k=2))
# r.shuffle(city)
# print(city)
#
# # s = [8, 7, 6, 2, 3, 5, 1, 4, 23, 54, 12]
# # print(r.choice(s))
# # print(r.choices(s, k=4))

# from random import randint
# print([randint(20, 50) for i in range(10)])

# s = [8, 7, 9, 6, 2, 1, 3, 4, 12, 23, 43, 13]
# print(sum(s))
# print(len(s))
# print(min(s))
# print(max(s))


# s = [71, 19, 22, 88, 27, 52, 50, 10, 19]
# print(s)
# max_el = max(s)
# print(max_el)
# print("Max: ", max(s))
# s.remove(max_el)
# s.insert(0, max_el)
# print(s)

# lst = []
# if not lst:  # len(lst) == 0:
#     print("Список пуст")
#
# print(bool(lst))

# from random import  randint
# n1 = int(input("Размер первого списка: "))
# n2 = int(input("Размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# s = a + b
# print("Третий список: ", s)
#
# s = []
# for i in range(len(a)):
#     if a[i] not in s:
#         s.append(a[i])
# for i in range(len(b)):
#     if b[i] not in s:
#         s.append(b[i])
# print("Элементы обоих списков: ", s)


# m = [
#     [1, 2, 3,4],
#     [5, 6, 7,8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(m[1][2])
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for i in m:
#     for j in i:
#         print(j ** 2, end='\t')
#     print()
# print()
# for i in m:
#     for j in i:
#         print(j, end='\t')
#     print()

# w, h = 5, 3
# m = [[x * y for x in range(w)] for y in range(h)]
# for i in m:
#     for j in i:
#         print(j*j, end='\t')
#     print()

# for x, y in [[1, 2], [3,4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# from random import randint
# w, h = 5, 4
#
# m = [[randint(10, 30) for x in range(w)] for y in range(h)]
# for i in m:
#     for j in i:
#         print(j, end='\t\t')
#     print()

# w, h = 3, 4
# m = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# res = 0
# for i in m:
#     for j in i:
#         if j < 0:
#             res += 1
#         print(j, end='\t\t')
#     print()
# print("Количество отрицательных элементов: ", res)


# import math
#
# num1 = math.sqrt(4)
# # num2 = round(5.92)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.9)
# print(num1)
# print(num2)
# print(num3)

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")

# sec = time.time()
# print(sec)
#
# local = time.ctime()
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))
#
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "sec")


# text = input("Название напоминанием: ")
# locale_time = float(input("Через сколько минут: "))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish =time.time()
# res = finish - start
# print(res)
#
# start = time.monotonic()
# time.sleep(5)
# finish =time.monotonic()
# res = finish - start
# print(res)


# Функция

# def hello(name):  #  Аргументы
#     print("Hello", name)
# hello("Ira")
# hello("Ivan")

# def get_sum(a, b):
#     print(a + b)
#
#
# a1 = 2
# b1 = 5
# get_sum(a1, b1)
# n = 10
# m = 20
# get_sum(n, m)

# def x(sym1, sym2, numb):
#     for i in range(numb):
#         if i % 2 == 0:
#             print(sym1, end='')
#         else:
#             print(sym2, end='')
#     print()
#
#
# x('+', '-', 9)
# x('x', 'o', 7)
# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# a1 = 2
# b1 = 5
# res = get_sum(a1, b1)
# print(res)

# def maxmin(one, two):
#     if one > two:
#         return one
#     else:
#         return two
# print(maxmin(9, 16))

# a = int(input("Введите сумму: "))
# b = int(input("Введите сумму: "))
# def maxmin(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
# res = maxmin(a, b)
# print(res)

# def cub(a):
#     return a * a *a
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# if func(10, 5):
#     print("1-ое число больше")
# else:
#     print("2-е число больше")


# def check_pass(pasword):
#     has_upper = False
#     has_lower = False
#     fas_num = False


#     for ch in pasword:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#
#         if len(pasword) >= 8 and has_upper and has_lower and has_num:
#             return True
#         return False
#
#
#
# p = input("Введите пароль: ")
# if check_pass(p):
#     print("Это надежный пароль")
# else:
#     print("Это не надежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def digital_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма чет цифр")
# print(digital_sum(9874023))
# print(digital_sum(38271))
# print(digital_sum(123456789))
# print("Сумма  не чет цифр")
# print(digital_sum(9874023, even=False))
# print(digital_sum(38271, even=False))
# print(digital_sum(123456789, even=False))


# def displate_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
# displate_info("Ira", 23)
# displate_info(23, "Ira")


# a = 2
# b = 2
# # print(a == b)
# print(a, id(a))
# print(b, id(b))
# a = 3
# b = 3
# print(a, id(a))
# print(b, id(b))
# print(a is b)
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1, id(lt1))
# print(lt2, id(lt2))
#
# # print(lt1 == lt2)
# print(lt1 is lt2)

# lt1 = [1, 2, 3]
# print(lt1, id(lt1))
# lt1.append(4)
# print(lt1, id(lt1))


# Кортеж (tuple)

# lst = [10, 20, 30]
# ltp = (10, 20, 30)
# print(lst)
# print(ltp)
#
# print(lst[0])
# print(ltp[0])
#
# lst[0] = 25
# print(lst)
# ltp[0] = 25
# print(ltp)


# lst = [10, 20, 30]
# ltp = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(ltp.__sizeof__())

# # a = 1, 2, 3, 4, 5, 6
# # a = tuple("hello")
# a = tuple((1, 2, 3, 4, 5, 6))
# print(a)
# # print(type(a))
#
# print(a[1:4])
# print(a)
# print(type(a))


# from random import  randint
# s = [input("==> ") for i in range(5)]
# print(s)
# s = tuple(input("==> ") for i in range(5))
# s = tuple(randint(0, 100) for i in range(5))
# print(s)


# t1 = tuple("Hello")
# t2 = tuple("World")
# t3 = t1 + t2
# print(t3)
# # # t4 = t1 * 3
# # # print(t4)
# # print(t3.count('l'))
# # print(t3.index('l'))
# # print(t3.index('l', 4))
#
# for i in t3:
#     print(i, end=' ')


# def slicer(any_tuple, element):
#     if element in any_tuple:
#         if any_tuple.count(element) > 1:
#             first_index = any_tuple.index(element)
#             second_index = any_tuple.index(element, first_index + 1) + 1
#             return any_tuple[first_index:second_index]
#         else:
#             return any_tuple[any_tuple.index(element):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import  randint
#
# def rnd_tpl(a, b):
#     s = tuple(randint(a, b + 1) for i in range(10))
#     return s
#
#
# n = rnd_tpl(0, 5)
# m = rnd_tpl(-5, 0)
# print(sorted(n))
# print(sorted(m))
# x = n + m
# print(x)
# print(x.count(0))

# t = (10, 11,[1, 2, 3], [4, 3, 6], ["Hello", "World"])
#
# print(t[4][0])
# t[4][0] = "New"
# t[4].append("hi")
# print(t)

# t = (1, 2, 3)
# # x = t[0]
# # z = t[1]
# # y = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# user = get_user()
# print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# first_name, year, married = user
# print(first_name, year, married)

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lt = list(tpl)
# print(lt)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326),("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2),("Марсель", 1.6))),
# )
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население: ", country_population, sep="")
#     for city in cities:
#         citi_name, city_population = city
#         print("\tГород", citi_name,", население: ", city_population)

#  Множество (set)

# s = {"banana", "apple", "orange", "apple", "orange"}
# print(s)

# a = set("Hello")
# print(a)
# print(type(a))

# s = ["banana", "apple", "orange", "apple", "orange"]
# print(s)
# s1 = set(s)
# print(s1)
# s2 = list(s1)
# print(s2)

# s = {x * x for x in range(10)}
# print(s)

# def to_set(el):
#     x = set(el)
#     return x, len(x)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 6, 2, 9, 11, 3, 4, 2]))

# t = {"red", "green", "blue"}
# # print("green" in t)
# for i in t:
#     print(i)


# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# print(r)
# # a = {i for i in r if 'a' in i}
# # a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r}
# a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r if i[1] == 'c'}
# print(a)
#
# r1 = ['ab_1', 'ac_2']
# r2 = ['bc_1', 'bc_2']
# print(r1 + r2)

# user = {"Tom", "Bob", "Max"}
# print(user)
# # user.remove("Tom")
# # user.discard("Tom")
# # user.pop()
# # user.clear()
# user.add("Ann")
# print(user)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}

# c = a.union(b)
# c = a | b
# print(c)
# a |= b
# print(a)
# c = a & b
# print(c)
# a &= b
# print(a)
# c = a - b
# print(c)
# a -= b
# print(a)
# c = a ^ b
# print(c)
# a ^= b
# print(a)

# ЗАДАЧА

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 |s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = set("Hello")
# s2 = set("How are you")
# z = s1 & s2
# print(z)


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)
# print(b >= a)

# drawing = {' Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
# only_one = drawing ^ music
# print(only_one)
# both = drawing & music
# print(both)
# drawing = drawing - both
# print(drawing)


# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
# a = frozenset({'hello', 'world'})
# print(a)

#  Словарь (Dict)

# s = ['a', 'b', 'c']  # Список
# d = {'one': 'a', 'two': 'b', 'three': 'c'}  # Словарь
# print(s)
# print(d)
# print(s[0])
# print(d['one'])

# d = {}
# users = (
#     ('one', 'a'),
#     ('two', 'b'),
#     ('three', 'c')
# )
# print(users)
# d = dict(users)
# print(d)
# print(type(d))


# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[0])
# d[0] = 15
# print(d)
# d[1] += 100
# print(d)


# d = {0: 'text', 'one': 45, (1, 2.3): 'кортеж', 42: [2, 3, 6, 7], True: 1, False: 0, 12: '45'}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)][2])
# del d[(1, 2.3)]
# print(d)
# print(42 in d)

# d = {'one': 'a', 'two': 'b', 'three': 'c'}
# # for i in d:
# #     print(i, "-->", d[i])
#
# key = 'one'
# try:
#     del d[key]
# except KeyError:
#     print("Нет такого ключа " + key + " в словаре")
# print(d)

# s = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for i in s:
#     res *= s[i]
# print(res)

# d =dict()  # []
# d[1] = input("==> ")
# d[2] = input("==> ")
# d[3] = input("==> ")
# d[4] = input("==> ")

# d = {i: input('=-> ') for i in range(1, 5)}
# print(d)
# disl = int(input("Какой элемент исключить: "))
# del d[disl]
# print(d)


# x = {
#     1: ['Core-i3-4330 - ', 9, '4500руб'],
#     2: ['Core-i5-4670K - ', 3, '8500руб'],
#     3: ['AMD FX-6300 - ', 6, '3700руб'],
#     4: ['Pentium G3220 - ', 8, '2100руб'],
#     5: ['Core-i5-3450 - ', 5, '6400руб']
# }
#
#
# def port():
#     for i in x:
#         print(f'{i}) {x[i][0]} - {x[i][1]} шт. по {x[i][2]}')
#
#
# port()
#
# while True:
#     j = int(input('№: '))
#     if j == 0:
#         break
#     else:
#         x[j][1] = int(input('Количество: '))
#
# port()

# d = {'one': 'a', 'two': 'b', 'three': 'c'}
# print(d.keys())
# print(d.values())
# print(d.items())
# # for i, j in d.items():
# #     print(i, "->", j)
#
# s = list(d)
# print(s)


# Методы словарей

# d = {'one': 'a', 'two': 'b', 'three': 'c'}
# # value = d['one']
# value = d.get('one1', 'Такого ключа нет')
# print(value)

# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
#
# d2['four'] = 'd'
# print("D =", d)
# print("D2 =", d2)

# d = {'one': 'a', 'two': 'b', 'three': 'c'}
# # item = d.pop('two', 'Такого ключа не существует')
# # print(item)
# # print(d)
# # item = d.popitem()
# # print(item)
# # print(d)
# # d.clear()
# # print(d)
# # a = {'four': 'd', 'two': 'last'}
# d.update([('four', 'd'), ('two', 'last')])
# print(d)


# x = {'a': 1, 'b': 2}
# y = {'b': 2, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# n = {'name': 'Kelly', 'age': '25', 'salary': '8000', 'city': 'NewYork'}
# m = dict()
# dolsit = dict()
# dolsit['age'] = n.pop('age')
# dolsit['local'] = n.pop('city')
# m['name'] = n.pop('name')
# m['salary'] = n.pop('salary')
# print(m)
# print(dolsit)

# x = {'один': 1, 'два': 2, 'Три': 3, 'Четыре': 4}
# d2 = {k: v for k, v in x.items() if v <= 2}
# print(d2)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'Free'
#     },
#     'second':{
#         4: 'Four',
#         5: 'Five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# x = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
# for i in x:
#     if type(i) == str:
#         d[i] = []  # d = {'one':[], "two":[], "three":[]}
#         s = i  # "one"
#     else:
#         d[s].append(i)  # d = {'one':[1,2,3],"two":[10,20] и.т.д}
# print(d)


#  12.09.23


# a = {1, 2, 3, 4, 5}
# b = {'one', 'two', 'three'}
# c = [4.0, 5.5, 6.2]
# d = list(zip(a, b, c))
# print(d)

# one = {'name': 'Igor', 'surname': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'surname': 'Smith', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "-->", v1)
#     print(k2, "==>", v2)

# pa = [(4, 'three'), (2, 'one'), (6, 'two')]
# a, b = zip(*pa)
# print(a)
# print(b)
#
# data = list(zip(b, a))
# print(data)
#
# data.sort()
# print(data)
#
# data = dict(data)
# print(data)
#
# f = {v: k for k, v in data.items()}
# print(f)
#
# f = list(f.items())
# print(f)

# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.25, 'onion': 0.55}
# print({**one, **two})  # {{'apple': 0.45, 'orange': 0.35}, {'pepper': 0.25, 'onion': 0.55}}
#
# for k, v in {**one, **two}.items():
#     print(k, '==>', v)

# colors = ['red', 'blue', 'green']
# for i in range(len(colors)):
#     print(i + 1, ") ", colors[i], sep="")
# print()
# j = 1
# for color in colors:
#     print(j, ") ", color, sep="")
#     j += 1
# print()
# for v, color in enumerate(colors, start=1):
#     print(v, ") ", color, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))


# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(5, 9, 4))

# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


# def ch(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 5, 9, 7))

# def print_score(stud, *score):
#     print("Students Name: ", stud)
#     for scores in score:
#         print(scores)
#
#
# print("Jonathan", 100, 95, 88, 92, 99, 65)
# print("Tom", 96, 20, 30, 56)

# def func(**kwargs):
#     print(kwargs)
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))


# def info(**data):
#     for k, v in data.items():
#         print(k, "-->", v)
#
#
# info(surnam="Sharm", name="Yato", age=22, phone=89233334565)
# info(surnam="Window", name="Yana", email="Anna@myaucat.ru", country="Russian", age=21, phone=89233564535)


# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='bob', age=31, weight=61, eyes_calors='grey')
# print(my_dict)


# name = "Tom"

# def hi():
#     global name
#     name = "Sam"
#     surname = "Jons"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5

# def add(a):
#     x = 2
#
#     def add_some():
#         print("x =", x)
#         return a + x
#
#     return add_some()
#
#
# print(add(3))
#
# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# lst = [5, 2, 3, 4, 5, 6]
# print(sum(lst))

# prin = 5
# s = 2
# print(s)

# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World")


# def fun1():
#     a = 6
#
#     def func2(b):
#         a = 4
#         print("Сумма:", a + b)
#
#     print("a:", a)
#     func2(4)
#
#
# fun1()


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a:", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# c = x + t
# print(c)


# 14.09.23


# x = 5
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x', x)  #33
#
#     fn2()
#     print('fn1.x', x)  # 25
#
#
# fn1()
# print("x =:", x)

# def outer(a1, b1, a2, b2):
#     a = 0  # 1
#     b = 0  # 7
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # []


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = outer(5)
# print(a(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def city(s):
#     с = 0
#
#     def inner():
#         nonlocal с
#         с += 1
#         print(s, с)
#
#     return inner
#
#
# res1 = city('Москва')
# res1()
# res1()
# res2 = city('Сочи')
# res2()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Zax': 85,
#     'Daz': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Gras': 69
# }

# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# b_A = outer(80, 100)
# b_B = outer(70, 80)
# b_C = outer(50, 70)
# b_D = outer(0, 50)
# print('A: ', b_A(students))
# print('B: ', b_B(students))
# print('C: ', b_C(students))
# print('D: ', b_D(students))


# def outer(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj = outer(5, 2)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())


# Анонимные функции(lambda - Выражение)

# func = lambda x, y: x + y  # Не правильно
# print(func(1, 2))


# print((lambda x, y: x + y)(1, 2))  # Правильно

# print((lambda x, y: (x ** y) - 3)(2, 5))


# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c = 3: a + b + c)(10, 20))
# print((lambda a, b = 2, c = 3: a + b + c)(10))
# print((lambda a = 1, b = 2, c = 3: a + b + c)())
# print((lambda *args: sum(args))(10, 20, 30))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for t in c:
#     print(t('abc__'))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(10)
# print(f(5))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# f1 = outer1(10)
# print(f1(5))
#
# outer2 = lambda n: lambda x: n + x
# f2 = outer2(10)
# print(f2(5))
#
# print((lambda n: lambda x: n + x)(10)(5))


# print((lambda n: lambda x: lambda z: n + x + z)(4)(2)(6))

# d = {'b': 25, 'a': 15, 'c': 24}
# # lst = list(d.items())
# # print(lst)
# # lst.sort(key=lambda i: i[1])
# # print(lst)
#
# new_d = sorted(d.items(), key=lambda i: i[1])
# print(new_d)
# print(dict(new_d))

# players = [
#     {'namae': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'namae': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'namae': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'namae': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
# res = sorted(players, key=lambda i: i['last name'])
# print(res)
# res1 = sorted(players, key=lambda i: i['rating'], reverse=True)
# print(res1)
# # res2 = sorted(players, key=lambda i: i['rating'], reverse=True)
# res2 = min(players, key=lambda i: i['rating'])
# # res2 = max(players, key=lambda i: i['rating'])
# print(res2)
#
# # a = [1, 2, 3]
# # print(sum(a, 12))


# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[0](12, 2))
# print(a[-1](12, 2))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье'),
# }
# d[4]()


# area = {
#     'circle': lambda r: 3.14 * r ** 2,
#     'triangle': lambda a, b: a * b
#
# }
# print('', area['circle'](2))

# print((lambda a, b, c: a if (a <= b) and (a <= c) else b if (b <= a) and (b <= c) else c)(9, 8, 5))


#  map(func, *iter), filter(func, *iter)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))


# t = (2.28, 6.44, 100.4)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))


# 19.09.23


# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# st = ['a', 'b', 'c', 'd', 'e', ]
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: (x, y), st, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# filter(func, *iter)

# t = ('xabc', 'zab', 'abcda', 'def', 'qad',)
# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# t2 = tuple(filter(lambda s: s * 2, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# from random import randint
#
# b = [randint(1, 40) for i in range(10)]
# res = list(filter(lambda s: 10 <= s <= 20, b))
# print(res)


# Декораторы


# def hello():
#     return "Hello, I'am func 'Helloz'"
#
#
# def super_func(func):
#     print("Hello, I'am func 'supr_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I'am func 'Helloz'"
#
#
# # test = hello
# # print(test())


# def my_decor(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code auto')
#
#     return wrap
#
#
# def func_test():
#     print("Hello, I'am func 'func_test'")
#
#
# test = my_decor(func_test)
# test()

# def my_decor(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code auto')
#
#     return wrap
#
#
# @my_decor
# def func_test():
#     print("Hello, I'am func 'func_test'")
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italik(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italik
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def args_decor(fn):
#     def wrap(args1, args2):
#         print(args1, args2)
#         fn(args1, args2)
#
#     return wrap
#
#
# @args_decor
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лазарева")


# def args_decor(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decor
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name('Борис', 'Елизовета', 'Светлана', study="JavaScript")
# print_full_name('Владимир', 'Екатерина', 'Виктор')

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def fran(args1):
#     def decor(func):
#         def wrap(args2):
#             print(args1, "=", func(args2) * args1)
#
#         return wrap
#
#     return decor
#
#
# @fran(3)
# def return_num(num):
#     print("Результат:", num, "*", end=" ")
#     return num
#
#
# return_num(5)


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Не корректный тип данных", f_args[i])
#                 for k in kwargs:
#                     if type(f_kwargs[k]) != kwargs[k]:
#                         raise TypeError("Не корректный тип данных", f_kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!! "):
#     return (x + y) * z
#
#
# print(typed_fn(3, 5, 6))
# # print(typed_fn(3, 5, "Doge"))
# # print(typed_fn(3.6, 4.5, 7.8))
# print(typed_fn2("Hello, ", "world", "!!"))
# print(typed_fn3("Hello, ", "world", z=5))


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# # print(e[::-1])
# # print(e*3)
# e = e[:3] + 't' + e[4:]
# print(e)

# def changeCharTostr(s, c_old, c_new):
#     s2 = ""
#
#     for i in s:
#         if i == c_old:
#             s2 += c_new
#             continue
#         s2 += i
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# # str2 = 'Я изучаю Python. Мне нравится Python. Python очень интересный язык программирования.'
#
# str2 = changeCharTostr(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)


# print("Привет")
# print(u"Привет")
# print("C:\\folder\\filter.txt")

# print(r"C:\folder\filter.txt")
# print(r"C:\folder\\"[:-1])
# print(r"C:\folder" + "\\")
# print("C:\\folder\\")

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне" + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")
#
# print(f"{round(3.12314, 2)}")
# print(f"{3.12314:.2f}")

# x = 10
# y= 5
# print("x =", x)
# print(f"{x = }, {y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# num = 74
# print(f"{{{num}}}")
# print(f"{{{{{num}}}}}")


# dir_name = "folder"
# file_name = "File.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home" + "\\" + dir_name + "\\" + file_name)

# s = """<div>
# <a href="#">content</a>
# </div>"""
# print(s)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра, на основании заданной высоты, и радиуса основания
#
#     :param r: Положительное число, радиус основания цилиндра
#     :param h: Положительное число, высота цилиндра
#     :return: Положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('А'))
# print(ord('Я'))
# print(ord('а'))

# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("--> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(75))

# a = 122
# b = 97
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))

# print("apple" == "Apple")
# print("apple" > "Apple")

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASC = 33
# MAX_ASC = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(rand_len):
#         rand_char = chr(randint(MIN_ASC, MAX_ASC))
#         res += rand_char
#     return res
#
#
# print("Случайный пароль:", random_password())


# s = "hello, WORLD! I am learning Python."
# # print(s.capitalize())  # Hello, world! i am learning python.
# # print(s.lower())  # hello, world! i am learning python.
# # print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# # print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# # print(s.title())  # Hello, World! I Am Learning Python.
#
# # print(s.count('h', 1, -4))  # Считает строковых символов
# # print(s.find("l", 4, 19))  # (-1 нет совпадений)
# # print(s.index("Python"))  # Номер строки
# print(s.find("l"))  # Поиск с лева
# print(s.rfind("l"))  # Поиск с права
# print(s.index("l"))
# print(s.rindex("l"))


# text = input("Введите два слова через пробел: ")
# new_text = text[text.find(' ') + 1:]+' '+text[:text.find(' ')]
# print(new_text)

# s = "hello, WORLD! I am learning Python."
# ...
# print(s.index("I am"))
# print(s.startswith("I am", 14))
# print(s.endswith("Python."))


# print('abc123'.isalnum())  # цифры и буквы
# print('ABCabc'.isalpha())  # Буквы верхнем или нижнем регистре
# print('123'.isdigit())  # Чисто только цифры

# print('abc'.islower())  # Проверка на регистр
# print('ABC'.isupper())  # Проверка на регистр

# print('py'.center(10))
# print('py'.center(10, "-"))


# print("             py".lstrip())  # Удаляют пробелы с лева
# print("py             ".rstrip())  # Удаляют пробелы с права
# print("      py       ".strip())   # Удаляют пробелы с лева и права
# print('https://www.python.org'.lstrip("/:pths"))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python"))


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
# print("..".join(['1', '2', '3']))
# print(":".join("Hello"))

# print('Строка раздельная пробелами'.split())


# s = input("ФИО:").split()
# print(s[0], s[1][0], s[2][0])

# Регулярные выражения
# import re

#
# s = "Я ищю совпадения в 2023 году. И я их найду в 2 счёта."
# reg = ' '
# print(re.findall(reg, s))  # список содержащий все совпадения
# print(re.search(reg, s))  # место первого совпадения
#
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
#
# # print(re.match(reg, s))  # поиск по заданному шаблону в начале строки
#
# print(re.split(reg, s))  # сплит возвращяет список строк разбитых по шпблону разделителю
#
# print(re.sub(reg, "!", s, 3))  # поиск и замена

# s = "Я ищю совпадения в 2023 году. И я их найду в 2 счёта. 9178 [H^el_lo]"
# # reg = '[12][0-9][0-9][0-9]'
# # reg = '[а-яА-яё]'
# # reg = r'[A-Za-z.\[\]]'
# reg = r'[^0-9]'
# # reg = r'\.'
# print(re.findall(reg, s))

# t = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# p = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(p, t))

# s = "Я ищю совпадения в 2023 году. И я их найду в 2 счёта. 9178 [H^el_lo]"
# reg = r'\d+'
# print(re.findall(reg, s))


# d = 'Цифры: 7, +17, -42, 0013, 0.34'
# print(re.findall(r'[+-]?\d+\.?\d*', d))


# s = "09-09-1987 # Дата рождения"
# print("Дата рождения:", re.sub("#.+", "", s))

# s = "Дата рождения: 09-09-1987"
# print(re.sub("-", ".", s))

# s = "09-09-1987 # Дата рождения"
# print("Дата рождения:", re.sub("-", ".", re.sub("#.+", "", s)))

# s = "12 сентября 2023 года"
# reg = r'\d{2,4}'
# print(re.findall(reg, s))

# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 4578, 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))

# s = "Я ищю совпадения в 2023 году. И я их найду в 2 счёта."
# # reg = r'\w+\s\w+'
# reg = r'\w+\.$'
# print(re.findall(reg, s))

# def validate_login(name):
#     return re.findall('^[A-Za-z_-]{3,16}$', name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('Python_master'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))
# print(re.findall(r'\w+', '12 + й', flags=re.A))

# text = 'hello world'
# print(re.findall(r'\w\+', text, re.DEBUG))

# s = "Я ищю совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'я'
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))

# text = """
# one
# two
# """

# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall(r'one.\w+', text, re.S))

# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))
# print(re.findall(r'one$', text, re.M))

# print(re.findall("""
# [a-z.-]+  # part 1
# @         # @
# [a-z.-]+  # part 2
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python
# python
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))
# *?, +?, ??
# {m, n}?, {n}?, {m,}?


# s = "<p>Изображение <img alt='картинка' src='bg.jpg'>- фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Ирина"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r'\w+\s*=\s*\d[.\w]*'
# # reg = r'(?:int|double)\s*=\s*\d[.\w]*'
# reg = r'((int|double)\s*=\s*\d[.\w]*)'
# print(re.findall(reg, s))
# (?:)-Делает круглые скобки не сохраняющие
# ()- сохраняющие скобки

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# s = '28-08-2021'
# reg = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(20[0-9][0-9])'
# print(re.findall(reg, s))

# s = "Я ищю совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'(\d+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s))
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(re.search(reg, s).group(1))

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f'<option value="{count}">{m.group(1)}</option>\n'
#
#
# print("<select>")
# print(re.sub(r"\s*(\w+)\s*", repl_find, text))
# print("<select>")


# s = "<p>Изображение <img alt='картинка' src='bg.jpg'>- фон страницы</p>"
# # reg = r'<img\s+[^>]*src\s*=\s*([\'"])(.+?)\1>'
# reg = r'<img\s+[^>]*src\s*=\s*(?P<q>[\'"])(.+?)(?P=q)'
# print(re.findall(reg, s))
#
# # (?P<name>)  (?P=name)

# s = "Самалет прилетает 10/23/2023. Будем рады вас видеть после 10/24/2023."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
#
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
#
# print(re.sub(reg, r'http://\1', s))


#  05/10/2023

# Файлы

# f = open("texttext.txt")
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)


# f = open(r"D:\pyth\texttext.txt")
# f = open(r"D:\\pyth\\texttext.txt")
# f = open("texttext.txt")
# print(f.read(3))
# print(f.read())
# f.close()

# f = open("one.txt", 'r')
# print(f.readline())
# print(f.readline())
# f.close()

# f = open("one.txt", 'r')
# print(f.readlines())
# f.close()

# f = open("one.txt", 'r')
# for line in f:
#     print(line, end="")
# f.close()

# f = open("one.txt", 'r')
# for line in f:
#     print(line, end="")
#     count += 1
#     # print(f.readlines())
#     # print(len(f.readline()))
# f.close()
# print(count)

# f = open('xyz.txt', 'w')
# f.write("Hello \nWorld")
# f.close()
#
# f = open('xyz.txt', 'a')
# print(f.write("\nNew Text"))
# f.close()

# f = open('xyz.txt', 'a')
# line = ['\nThis is line 1', '\nThis is line 2']
# f.writelines(line)
# f.close()


# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)  # '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]'
# # t = "\t".join(map(str, lst))
# # print(t)
# # f.write(t)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open('zadacha.txt', 'w')
# f.write("Заменить строки с текстом файле;\nизменить строку в списке;\nзаписать список файл;\n")
# f.close()
#
# f = open('zadacha.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello World\n"
# f.close()
#
# f = open('zadacha.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('zadacha.txt', 'w')
# f.write("Заменить строки с текстом файле;\nизменить строку в списке;\nзаписать список файл;\n")
# f.close()


# pos = int(input('del = '))
# f = open('zadacha.txt', 'r')
# l = f.readlines()
# if (pos >= 0) and (pos < len(l)):
#     i = pos
#     while i < len(l) - 1:
#         l[i] = l[i + 1]
#         i = i + 1
#     l = l[:1]
# f.close()
#
# f = open('zadacha.txt', 'w')
# for line in l:
#     f.write(line)
#
# f.close()

# f = open('zadacha.txt', 'r')
# int_put = int(input("Числа: "))
# read_file = f.readlines()
# if 0 <= int_put < len(read_file):
#     del read_file[int_put]
# else:
#     print("Индекс введен не верно!")
# print(read_file)
# f.close()

# f = open("texttext.txt", 'r')
# print(f.read(3))
# print(f.tell())  # Позиция условного курсора
# print(f.seek(1))
# print(f.read())
# f.close()

# f = open("texttext.txt", 'r+')
# print(f.write('I am learning Python'))  # 20
# print(f.seek(3))  # 3
# print(f.write("-new string-"))  # 12
# print(f.tell())  # 15
# f.close()

# with open('texttext.txt', 'w+') as f:
#     print(f.write('0123456789'))
#
# with open('texttext.txt', 'r') as f:
#     for line in f:
#         print(line)


# file = "res1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     return " ".join(map(str, lt))
#
#
# with open(file, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")
#
# with open(file, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# nums_list = list(map(float, nums.split()))
# print(nums_list)
# print(sum(nums_list))
# print(len(nums_list))
# print(sum(nums_list) / len(nums_list))


# def long_words(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(long_words("texttext.txt"))


# read_file = "one.txt"
# write_file = "two.txt"
# therd_file = "threez.txt"
#
# text = "Строка№1\nСтрока№2\nСтрока№3\nСтрока№4\nСтрока№5\nСтрока№6\nСтрока№7\nСтрока№8\nСтрока№9\nСтрока№10\n"
#   with open("one.txt", 'w') as f:
#      f.write(text)
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line. replace("Строка", "Линия -")
#         fw.write(line)

# read_file = "one.txt"
# write_file = "two.txt"
# therd_file = "threez.txt"
#
# with open(read_file, 'r') as f1, open(write_file, 'r') as f2, open(therd_file, 'w') as f3:
#     file_1 = f1.readlines()
#     file_2 = f2.readlines()
#     f4 = file_1 + file_2
#     f3.writelines(f4)


# Модуль OS и OS.PATH

# import os
# import os.path


# print(os.path.split(r"D:\pyth\nested\nested2\text.txt"))

# print(os.getcwd())  # возвращает путь к текущей директории
# print(os.listdir())  # список файлов и директории
# print(os.listdir(".."))

# os.mkdir("folder_2")  # создание директории(папки)
# os.mkdir("nested1/nested2/nested3")  # Создаст не только конечную директорию, но и конечную

# os.rmdir("folder")  # удаляем только пустую папку

# os.rename('xyz.txt', 'numbz.txt')  # переименовывает название файла или папки
# os.rename('numbz.txt', 'folder/numbz.txt')  # перемещение файла в папку

# os.renames('', '')  # перемещяет и создает папку

# os.remove('')  # удаление файла

# for root, dirs, files in os.walk("nested", topdown=False):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)
#     print()

# def remove_enpty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория с заданным название root удалена.")
#
#     print('-' * 50)
#
#
# remove_enpty_dirs("nested")

# import os


# print(os.path.split(r"D:\pyth\nested\nested2\text.txt"))
#
# print(os.path.dirname(r"D:\pyth\nested\nested2\text.txt"))
# print(os.path.basename(r"D:\pyth\nested\nested2\text.txt"))
#
# print(os.path.join(r"D:\pyth", "files", "folder", "dir", "two.txt"))

# import os
#
# # dirs = [r'Work\F1', r'Work\F2\F21']
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fls in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(fls)
#     print("-" * 50)


# print_tree("Work", topdown=False)
# print_tree("Work", topdown=True)


# # Work\w.txt
# # Work\F1\f11.txt
# # Work\F1\f12.txt
# # Work\F1\f13.txt
# # Work\F2\F21\f211.txt
# # Work\F2\F21\f212.txt


# import os


# print(os.path.exists(
#  r'D:\pyth\nested\nested2\text.txt'))  # Возвращается True, если path указывает на сущ путь в файловой системе
# print(os.path.isfile(r'D:\pyth\nested\nested2\text.txt'))  # проверка на наличие по заданному пути файла
# print(os.path.isdir(r'D:\pyth\nested\nested2'))  # проверка на наличие по заданному пути папки

# path = 'main.py'
# print(os.path.getsize(path))  # 67164 - В байтах
# print(os.path.getsize(path) / 1024)
# print(os.path.getatime(path))  # последний доступ к файлу
# print(os.path.getmtime(path))  # последнее изменение файла(windows) или  время последнего изм(Unix)
# print(os.path.getctime(path))  # время последнего изм в сек
#
# c = os.path.getmtime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getsize(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getsize(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getsize(path))))

# file_path = 'nested/nested2/res1.txt'
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f"{name} ({dirs}) время последнего доступа к файлу {atime}")
# else:
#     print(f"Файл {file_path} не существует")


# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("==>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(255, 2))

# 12.10.23
# РАЗОБРАТЬСЯ ДОМА С 1-ым ПРИМЕРОМ!!!!
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))
# # print(len(names))
# # print(names[1])
# # print(isinstance(names[1], list))
# # print(names[1][1])


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" HELLO\tWORLD "))


# class Point:
#     x = 1
#     y = 2
#
#
# p1 = Point()
# print(p1.x)
# print(p1.y)
#
# p1.x = 5
# p1.y = 7
# p2 = Point()
# print(p2.x)
# print(p2.y)
# print(p1.x)
# print(p1.y)
#
# print(id(Point))
# print(id(p1))
# print(id(p2))


# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# # Point.set_coord(p1, 5, 10)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coord(3, 7)
# print(p2.__dict__)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, *"*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона:{self.phone}\nСтрана: {self.country}"
#               f"\nГород: {self.city}\nАдрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, addres):
#         self.name = first_name
#         self.address = addres
#         self.birthday = birthday
#         self.phone = phone
#         self.city = city
#         self.country = country
#
#     def set_phone(self, phone):  # устанавливаем значение
#         self.phone = phone
#
#     def get_phone(self):  # получаем значение
#         return self.phone
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
# h1.print_info()
# h1.set_phone("55-99-11")
# h1.print_info()
# print(h1.get_phone())
# h1.set_name("Валерия")
# print(h1.get_name())


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __del__(self):
#         print("Удаление экземпляра класса")
#
#     def print_info(self, ):
#         print("Данные сотрудник:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(2, 8)
# p3 = Point(7, 12)
# # print(p3.count)
# # print(p2.count)
# # print(p1.count)
# print(Point.count)
# print(p1.x)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация робота: {self.name}")
#         Robot.k += 1
#
#     def say_hi(self):
#         print(f"Приветствую!! Меня зовут {self.name}")
#
#     def __del__(self):
#         print(f"{self.name} выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(f"{self.name} был последний")
#             print(f"Работающих роботов осталось {Robot.k}")
#         else:
#             print("Работающих роботов:")
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print(f"Численность роботов {Robot.k}")
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print(f"Численность роботов {Robot.k}")
# droid3 = Robot("Syrak")
# droid3.say_hi()
# print(f"Численность роботов {Robot.k}")
#
# print(f"\nЗдесь роботы могут проделать какую-то работу\n")
#
# print(f"Роботы закончили свою работу. Давайте выключим")
#
# del droid1
# del droid2
# del droid3
#
# print(f"Численность роботов: {Robot.k}")


# class Point:
#     __slots__ = ["__x", "__y"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установили координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получили координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# # # print(p1.x, p1.y)
# # p1.x = 100
# # # p1.__y = "abc"
# # # print(p1.x, p1.__y)
# # print(p1.__dict__)
# # p1.set_coord(100, 200)
# # print(p1.__dict__)
# print(p1.get_coord())
# # # print(Point.__dict__)
# # # p1.__check_value(5)
# # # Модификаторы доступа
# # # public - self.x(открытое)
# # # protected - self._x(при наследование)
# # # private - self.__x(закрытое)

#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     def __get_x(self):
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойств")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 3
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, x):
#         self.x = 0
#         if isinstance(x, (int, float)):
#             self.x = x
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, new_x):
#         if isinstance(new_x, (int, float)):
#             self.__x = new_x
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__x * 2.205
#
#
# weight = KgToPounds(12)
# print(f"{weight.x} кг => {weight.to_pounds()} фунтов")
# weight.x = 41
# print(f"{weight.x} кг => {weight.to_pounds()} фунтов")


# 19.10.2023

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Number:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if d > mx:
#             mx = d
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print("Максимальное число:", Number.max(3, 5, 7, 9))
# print("Минимальное число:", Number.min(3, 5, 7, 9))
# print("Средне арифметическое число:", Number.average(3, 5, 7, 9))
# print("Факториал числа:", Number.factorial(5))

# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_data):
#         day, month, year = map(int, string_data.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # date2 = Date.from_string('23.10.2023')
# # print(date2.string_to_db())
# #
# # date3 = Date.from_string('27.12.2024')
# # print(date3.string_to_db())
# dates = [
#     '30.12.2023',
#     '30-12-2020',
#     '01.01.2021',
#     '12.31.2023'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         date_db = date.string_to_db()
#         print(date_db)
#     else:
#         print(f"Не правильная дата или формат строки с датой")


# class Account:
#     rate_usd = 0.013
#     rate_eu = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eu = 'EUR'
#
#     def __init__(self, surname, number, procent, summarub):
#         self.surname = surname
#         self.number = number
#         self.procent = procent
#         self.summarub = summarub
#         print(f"Счет №{self.number} Принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет №{self.number} Принадлежащий {self.surname} был закрыт.")
#
#     @staticmethod
#     def convert(summarub, rate):
#         return summarub * rate
#
#     @classmethod
#     def set_usr_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_uer_rate(cls, rate):
#         cls.rate_eu = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.summarub, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eu(self):
#         eu_val = Account.convert(self.summarub, Account.rate_eu)
#         print(f'Состояние счета: {eu_val} {Account.suffix_eu}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.summarub += self.summarub * self.procent
#         print("Проценты были успешно начислены!")
#         self.print_balans()
#
#     def withdraw_money(self, val):
#         if val > self.summarub:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.summarub -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balans()
#
#     def add_money(self, val):
#         self.summarub += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balans()
#
#     def print_balans(self):
#         print(f"Текущий баланс {self.summarub} {Account.suffix}")
#
#     def print_info(self):
#         print(f"Информация о счете:")
#         print("-" * 20)
#         print(f"№{self.number}")
#         print(f"Владелец:{self.surname}")
#         self.print_balans()
#         print(f"Проценты: {self.procent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eu()
# print()
# Account.set_usr_rate(2)
# acc.convert_to_usd()
# Account.set_uer_rate(3)
# acc.convert_to_eu()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percent()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# acc.withdraw_money(3000)
# print()


# class Account:
#     rate_usd = 0.013
#     rate_eu = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eu = 'EUR'
#
#     def __init__(self, surname, number, procent, summarub):
#         self.surname = surname
#         self.__number = number
#         self.procent = procent
#         self.summarub = summarub
#         print(f"Счет №{self.number} Принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет №{self.number} Принадлежащий {self.surname} был закрыт.")
#
#     @property
#     def number(self):
#         return self.__number
#
#     @number.setter
#     def number(self, val):
#         self.__number = val
#
#     @staticmethod
#     def convert(summarub, rate):
#         return summarub * rate
#
#     @classmethod
#     def set_usr_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_uer_rate(cls, rate):
#         cls.rate_eu = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.summarub, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eu(self):
#         eu_val = Account.convert(self.summarub, Account.rate_eu)
#         print(f'Состояние счета: {eu_val} {Account.suffix_eu}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.summarub += self.summarub * self.procent
#         print("Проценты были успешно начислены!")
#         self.print_balans()
#
#     def withdraw_money(self, val):
#         if val > self.summarub:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.summarub -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balans()
#
#     def add_money(self, val):
#         self.summarub += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balans()
#
#     def print_balans(self):
#         print(f"Текущий баланс {self.summarub} {Account.suffix}")
#
#     def print_info(self):
#         print(f"Информация о счете:")
#         print("-" * 20)
#         print(f"№{self.number}")
#         print(f"Владелец:{self.surname}")
#         self.print_balans()
#         print(f"Проценты: {self.procent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eu()
# print()
# Account.set_usr_rate(2)
# acc.convert_to_usd()
# Account.set_uer_rate(3)
# acc.convert_to_eu()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percent()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# acc.withdraw_money(3000)
# print()

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, pa, weight):
#
#         self.fio = fio
#         self.old = old
#         self.password = pa
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должен быть строкой")
#         f = fio.split()
#         # print(f)
#         if len(f) != 3:
#             raise TypeError("Не верный формат ФИО")
#         letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("Можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_pa(pa):
#         if not isinstance(pa, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = pa.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Не верный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, val):
#         self.verify_old(val)
#         self.__old = val
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, pa):
#         self.verify_pa(pa)
#         self.__password = pa
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.__weight = w
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Рыцарев Игорь Николаевич"
# print(p1.fio)
# print(p1.__dict__)


#  НАСЛЕДОВАНИЕ

# class Point:
#     """Точка в двухмерном пространстве"""
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# print(issubclass(Point, object))
# print(Point.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисованный прямоугольник: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисованный прямоугольник: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# # line.draw_line()
# #
# # rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         # print("Инициализатор базового класса")
#         self._sp = sp  # self._sp = Point(1, 2)
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# line.set_coord(Point(20.3, 30), Point(100,200))
# line.draw_line()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class Rectfon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.bord = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.bord)
#
#
# shape1 = Rectfon(400, 200, "red")
# shape1.show_rect()
#
# shape2 = RectBorder(400, 200, "1px solid red")
# shape2.show_rect()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


# ПРЕРЕГРУЗКА МЕТОДОВ


# def func(a, b=None, c=None):
#     ...
#
#
# func(1, 2, 3)
# func(1, 2)
# func(1)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         # print("Инициализатор базового класса")
#         self._sp = sp  # self._sp = Point(1, 2)
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#     def set_coord(self, sp=None, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координата должны быть целочисленная")
#         elif sp is None:
#             if ep.is_int():
#                 self._ep = sp
#             else:
#                 print("Координата должны быть целочисленная")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целочисленными")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# line.set_coord(Point(20.3, 30), Point(100, 200))
# line.draw_line()
#
# line.set_coord(ep=Point(100, 300))
# line.draw_line()

# Абстрактные методы
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         # print("Инициализатор базового класса")
#         self._sp = sp  # self._sp = Point(1, 2)
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def draw(self):
#         raise NotImplemented("В дочернем классе должен быть определен метод draw()")
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(30, 20)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
#
# for f in figs:
#     f.draw()


# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# from math import pi
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t3 = RoundTable(radius=20)
# print(t3.__dict__)
# print(t3.calc_area())


# АБСТРАКТНЫЙ КЛАСС

# from abc import ABC, abstractmethod


# class Chees(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Queen(Chees):
#     def move(self):
#         print("Ферзь перемещен на клетку")
#
#
# # q = Chees()
# q = Queen()
# q.move()
# q.draw()

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EU"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(f"{Euro.suffix} = {self.convert_to_rub():.2f} RUB")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")
#
# print("*" * 50)
# for elem in e:
#     elem.print_value()


#  Интерфейс


# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#
#
# class Grandchild(Child):
#     def display2(self):
#         print("GrandChild Class")
#
#
# gc = Grandchild()
# gc.display1()
# gc.display2()


#  Вложенный класс

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         return "Метод внешнего класса"
#
#     def outer_obj(self):
#         return "Метод экземпляра"
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print(MyOuter.age, MyOuter.outer_method(), self.obj.outer_obj(), self.obj.name)
#
#
# out = MyOuter("внешний")
# inner = out.MyInner("внешний", out)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "LightGreen"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()


# class Inter:
#     def __init__(self):
#         self.name = "Smith"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Inter()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Ara"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# d2 = outer.head
# print()
# d1.display()
# print()
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Outer")
#
#     class Inner:
#         def __init__(self):
#             self.iner_iner = self.InnerClass()
#
#         def show(self):
#             print("Inner")
#
#         class InnerClass:
#             def show(self):
#                 print("InnerClass")
#
#
# out = Outer()
# out.show()
#
# inner2 = out.inner.iner_iner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "intel"
#
#         def model(self):
#             return "core-i7"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         print("Инициализатор басе")
#         self.db = self.Inner()
#
#     def display(self):
#         print("Base")
#
#     class Inner:
#         def display1(self):
#             print("Inner in Base")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("SubClass")  # отработал
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner in SubClass")
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coord = args  # ()
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 7)
# print(len(p))
# p2 = Point(2, 4, 9)
# print(len(p2))

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(2, 7)
# print(pt.x)
# print(pt.y)
# pt.length = 10
# print(pt.__length)
# # pt.z = 5
# # print(pt.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2(1, 2)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = ('z',)
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(2, 6)
# print(pt3.x)
# pt3.z = 30
# print(pt3.z)


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def __init__(self, name):
#         self.name = name
#
#     def bark(self):
#         print(self.name + " is barks")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.play()
# beast.sleep()


# class A:
#     def __init__(self):
#         print("Инициатор класса А")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициатор класса B")
#
# class C(A):
#     def __init__(self):
#         print("Инициатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициатор класса D")
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# line1.draw()
#
# print(Line.__mro__)


# 02.11.23
#  Миксимы

# class Displaer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LogerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displaer.display(message)
#         self.log(message)
#
#
# class MySubClass(LogerMixin, Displaer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclass.txt')
#
#
# subclass = MySubClass()
# subclass.display("Эта строка будет печататься и записываться в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 36000)
# n.print_info()
# n.save_sell_log()
# n2 = NoteBook("HP", 1.5, 36000)
# n2.save_sell_log()


#  Перегрузка операторов

# число секунд в одном дне 24*60*60=86400сек


# Дома доделать
# class Clock:
#     __Day = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__Day
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Не верный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должен быть целым числом")
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# x1 = Clock(80000)
# print(x1.get_format_time())
# x1["hour"] = 9
# x1["min"] = 61
# x1["sec"] = 32
# print(x1["hour"], x1["min"], x1["sec"])
# print(x1.get_format_time())
# x2 = Clock(100)
# print(x2.get_format_time())
# # x1 += x2
# # print(x1.get_format_time())
# # x3 = x1 + x2
# # print(x3.get_format_time())
#
# # Проверка
# # if x1 == x2:
# #     print("Время одинаково")
# # else:
# #     print("Время разное")
#
# if x1 != x2:
#     print("Время разное")
# else:
#     print("Время одинаково")
# Дома до делать

# from random import choice, randint
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy"
#         elif self.pol == "F":
#             return f"{self.name} is good girl"
#         else:
#             return f"{self.name} is good kitty"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError("Типы не совместимы")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# print(cat1)
# print(cat2)
# print(cat1 + cat2)


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Не верный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым не отрицательным числом")
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Anna", 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[1])
# s1[2] = 4
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)


# 07.11.23

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return self.a * 4
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
# # print(t1.get_per_tr(), t2.get_per_tr())
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я кот. меня зовут {self.name}. Мой возвраст {self.age}."
#
#     def sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я собака. меня зовут {self.name}. Мой возвраст {self.age}."
#
#     def sound(self):
#         return f"{self.name} гав."
#
#
# c1 = Cat("Пушок", 2.5)
# # print(c1.info(), c1.sound())
# d2 = Dog("Мухтар", 4)
# # print(d2.info(), d2.sound())
# for animal in (c1, d2):
#     print(animal.info())
#     print(animal.sound())


# class Human:
#     def __init__(self, surname, name, age):
#         self._name = name
#         self._surname = surname
#         self._age = age
#
#     def info(self):
#         print(f'\n{self._surname} {self._name} {self._age} ', end='')
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, spec, group, ball):
#         super().__init__(surname, name, age)
#         self.spec = spec
#         self.group = group
#         self.ball = ball
#
#     def info(self):
#         super().info()
#         print(f'{self.spec} {self.group} {self.ball} ', end='')
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, spec, group, ball, diplom):
#         super().__init__(surname, name, age, spec, group, ball)
#         self.diplom = diplom
#
#     def info(self):
#         super().info()
#         print(f'{self.diplom}', end='')
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, spec, ball):
#         super().__init__(surname, name, age)
#         self.spec = spec
#         self.ball = ball
#
#     def info(self):
#         super().info()
#         print(f'{self.spec} {self.ball}', end='')
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()

# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()

# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.,; ")
# print(s1(" ?Hello, World! "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):  # string
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
# s2 = StringStrip("?:!.,; ")
# print(s2(" ?Hello, World! "))

# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self):
#         print("Перед вызовом")
#         self.fn()
#         print("После вызова")
#
#
# @MyDecorator
# def func():
#     print("text")
#
#
# func()

# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         res = self.fn(x, y)
#         return f"Перед вызовом\n{res}\nПосле вызова"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))

# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, a, b):
#         return self.fn(a, b) ** 2
#
#
# @Power
# def func(a, b):
#     return a * b
#
#
# print("Результат", func(2, 5))

# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         res = self.fn(*args, **kwargs)
#         return f"Перед вызовом\n{res}\nПосле вызова"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a + b + c
#
#
# print(func(2, 5))
# print(func1(2, 5, 6))
# print(func2(2, c=5, b=6))


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             res = fn(*args, **kwargs)
#             return f"{self.arg} {res}"
#         return wrap
#
#
# @MyDecorator("Произведение:")
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))
# print(func(12, 5))


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             res = fn(*args, **kwargs)
#             return res ** self.arg
#
#         return wrap
#
#
# @MyDecorator(3)
# def func(a, b):
#     return a * b
#
#
# print("Результат", func(2, 2))
# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, na, su):
#         self.na = na
#         self.su = su
#
#     @dec
#     def info(self):
#         print(f"{self.na} {self.su}")
#
#
# p1 = Person("Виталий", "Чертилов")
# p1.info()
# def decorator(cls):
#     class Wrapper(cls):
#         def double(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print(f"Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.double(4))


# Дескрипторы

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.__name = String(name)
#         self.__surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__na = value
#     #
#     # @property
#     # def sur(self):
#     #     return self.__sur
#     #
#     # @sur.setter
#     # def sur(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__sur = value
#
#
# p = Person("Ivan", "Peter")
# print(p.name.get())

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{self.name} должно быть строкой")
#         instance.__dict__[self.name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Peters")
# print(p.name)
# print(p.surname)

# 09.11.23


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата{coord} должна быть числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         Integer.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# print(p1.x, p1.y, p1.z)


# Мета класс


# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# MyList = type(
#     'Mylist',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
# lst = MyList()
# lst.append(5)
# lst.append(8)
# lst.append(9)
# print(lst, lst.get_length())

# Создание модулей

# from geom import rect, sq, tria
# from geom import sq
# from geom import tria

# from geom import *

# if __name__ == '__main__':
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = tria.Triangle(1, 2, 3)
#     t2 = tria.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#     for g in shape:
#         print(g.get_perimetr())

# from car import elcar
#
# if __name__ == '__main__':
#     e_car = elcar.ElCar("Tesla", "T", 2018, 9900, 100)
#     e_car.info()
#     e_car.description_battery()

# Сеарилизация(упаковка данных) и Десериализация(распаковка данных)

# marshal(*.pyc)
# pickle
# json

# dump() - сохраняет данные в открытый файл
# load() - считывание данных из файла

# dumps() - сохраняет данные в строку
# loads() - считывает данные из строки


# import pickle

#
# file_name = "basket.txt"
#
# shop_list = {
#     "Фрукты": ['яблоки', 'манго'],
#     "Овощи": ("морковь", "лук"),
#     "Бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, 'rb') as f:
#     shop_list_2 = pickle.load(f)
#
# print(shop_list_2)

# class Text:
#     num = 35
#     string = "Привет"
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#     d = {"first": 1, "second": 2}
#
#     def __str__(self):
#         return f"Число: {Text.num}\nСтрока: {Text.string}\nСписок: {Text.lst}\nКортеж: {Text.tpl}\nСловарь: {Text.d}"
#
#
# obj = Text()
#
# obj1 = pickle.dumps(obj)
# print(obj1)
#
# obj2 = pickle.loads(obj1)
# print(obj2)


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         atrr = self.__dict__.copy()
#         del atrr['c']
#         return atrr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# 14.10.23
# import json

# data = {
#     'name': 'Olga',
#     'age': 35,
#     20: None,
#     True: 1,
#     'hobbies': ('running', 'singing'),
#     'children': [{
#         'first_name': 'Alice',
#         'age': 6
#     }]
# }
# # with open("data_file.json", "w") as fw:
# #     json.dump(data, fw, indent=4)
# # with open("data_file.json", "r") as fw:
# #     json.dump(data, fw, indent=4)
#
# json_strig = json.dumps(data)
# print(json_strig)
# print(type(json_strig))
# data2 = json.loads(json_strig)
# print(data2)
# print(type(data2))


# x = {
#     "name": "Виктор"
# }
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))

# Дома
# from random import choice
#
#
# def gen_person():
#     key = ''
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(key) != 8:
#         key += choice(nums)
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {key: {
#         'name': name,
#         'tel': tel
#     }}
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("persons_json"))
#     except FileNotFoundError:
#         data = []
#     data.append(person_dict)
#     with open('persons_json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())
# Дома


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __str__(self):
#         # a = ""
#         # for i in self.marks:
#         #     a += str(i) + ", "
#         # return f"Студент: {self.name}: {a[:-2]}"
#         # a = ", ".join(map(str, self.marks))
#         # return f"Студент: {self.name}: {a}"
#         return f"Студент: {self.name}: {', '.join(map(str, self.marks))}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def adit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self, file_name):
#         data = {"name": self.name, "marks": self.marks}
#         with open(file_name, "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self, file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, gr):
#         self.students = students
#         self.gr = gr
#
#     def __str__(self):
#         # a = ""
#         # for i in self.students:
#         #     a += str(i) + "\n"
#         # return f"Студент:{a}"
#
#         return "\nГруппа: " + self.gr + "\n" + '\n'.join(map(str, self.students))
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def dump_group(self, file_name):
#         with open(file_name, "w") as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             json.dump(stud_list, f)
#
#     def upload_group(self, file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
# st1 = Student("Bodnya", 5, 4, 3, 4, 5, 3)
# st1.load_from_file("st1.json")
# st1.dump_to_json("st1.json")
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.adit_mark(2, 4)
# # print(st1)
# # print(st1.average_mark())
# st2 = Student("Nikolaenko", 2, 3, 5, 4, 2)
# st3 = Student("Birukov", 3, 5, 4, 3, 5, 4)
#
# sts = [st1, st2]
# my_group = Group(sts, "ГК Python")
# # print(my_group)
# my_group.add_student(st3)
# # print(my_group)
# my_group.remove_student(1)
# # print(my_group)
# group22 = [st2]
# my_group2 = Group(group22, "ГК Web")
# # print(my_group2)
#
# Group.change_group(my_group, my_group2, 0)
#
# # print(my_group)
# # print(my_group2)
#
# file = "group2.json"
# my_group2.dump_group(file)
# my_group2.upload_group(file)


# 16.11.23

# Парсинг


import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# # print(todos)
# # for i in todos:
# #     print(i)
#
# todos_by_user = {}
#
# for i in todos:
#     if i["completed"]:
#         try:
#             todos_by_user[i["userId"]] += 1
#         except KeyError:
#             todos_by_user[i["userId"]] = 1
# print(todos_by_user)
#
# top_user = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_user)
#
# max_complete = top_user[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_user:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
#
# max_users = " and ".join(users)
# print(max_users)
#
# s = "s" if len(users) > 1 else ""
#
# print(f"User{s} {max_users} completed {max_complete} TODOS")
#
#
# def keep(td):
#     is_complete = td["completed"]
#     has_max_count = str(td["userId"]) in users
#     return is_complete and has_max_count
#
#
# with open("filter_max_completed.json", "w") as f:
#     filter_todos = list(filter(keep, todos))
#     json.dump(filter_todos, f, indent=2)


# CSV (Coma Separated Values)


import csv

#
# with open("data.csv") as r_file:
#     file_reader = csv.DictReader(r_file)
#     count = 0
#     for row in file_reader:
#         print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#
#         print(f"\t{row[0]} - {row[1]} - {row[2]}")
#         count += 1
#     print(f"Всего в файле {count + 1} строки")

# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerow(data)


# with open("student1.csv", "w") as f:
#     name = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator='\r', fieldnames=name)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Женя", "Возраст": 6})
#     file_writer.writerow({"Имя": "Ваня", "Возраст": 45})
#     file_writer.writerow({"Имя": "Сережа", "Возраст": 21})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator='\r',
#                             fieldnames=data[0].keys())  # fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# # print(response.text)
#
# todos = json.loads(response.text)
# # for i in todos:
# #     print(i)
#
# with open('ff.csv', 'w') as f:
#     writer = csv.DictWriter(f, todos[0].keys(), delimiter=';', lineterminator='\r', )
#     writer.writeheader()
#     for i in todos:
#         writer.writerow(i)


# Парсинг 21/11/23

# from bs4 import BeautifulSoup

# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# # row = soup.find("div", class_="name").text
# # row = soup.find_all("div", class_="name")
# # row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# # row = soup.find("div", {"data-set": "salary"})
# # row = soup.find("div", id="whois")
# # row = soup.find("div", string="Alena").parent.parent
# # row = soup.find("div", string="Alena").find_parent(class_="row")
# # row = soup.find("div", id="whois3")
# # row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)
# # for i in row:
# #     print(i.text)


# def get_copyrigter(tag):
#     whois = tag.find("div", class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copyrigter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)

# import requests
#
# r = requests.get("https://ru.wordpress.org")
# # print(r.status_code)
# # print(r.headers)
# # print(r.headers['Content-Type'])
# # print(r.content)
# print(r.text)

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open("plugin.csv", "a") as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     s = soup.find(id="main").find_all("section", class_="plugin-section")[-1]
#     plugins = s.find_all("article", class_="plugin-card")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a").get("href")
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# 23/11/23
# import csv
# import requests
# from bs4 import BeautifulSoup

# import csv
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugin1.csv", "a", encoding="utf-8-sig") as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=";")
#         writer.writerow((data['name'], data['snippet'], data['active'], data['test_cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("article", class_="plugin-card")
#     for el in p1:
#         try:
#             name = el.find("h3").text
#         except AttributeError:
#             name = ''
#
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#         except AttributeError:
#             snippet = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except AttributeError:
#             active = ""
#
#         try:
#             test = el.find("span", class_="tested-with").text.strip()
#             test_cy = refine_cy(test)
#         except AttributeError:
#             test_cy = ""
#
#         data = {
#             'name': name,
#             'snippet': snippet,
#             'active': active,
#             'test_cy': test_cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(15, 50):
#         url = f"https://ru.wordpress.org/plugins/browse/popular/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# 2-я часть урока

# Эту часть кода писать в main.py

# from parsers import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# MVC
# Model(Модель)
# View(Вид или представление)
# Controller(Контролер)


# Сокет

# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def pars_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 405 Page Not Allowed\n\n', 404
#     return 'HTTP/1.1 200 Its ok!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found!</h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed!</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = pars_request(request)
#     headers, code = generate_headers(method, url)
#     body = URLS.get(url, 'Errors 404')
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == "__main__":
#     run()


# import sqlite3
#
# # con = sqlite3.connect("profile.db")
# # cur = con.cursor()
# #
# # cur.execute("""
# # """)
# # con.close()
#
# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS user(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # date TEXT
#     # )""")
# cur.execute("DROP TABLES users")


# 05.12.2023

import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
# con.close()

with sqlite3.connect("user.db") as con:
    cur = con.cursor()
    cur.execute("""
    ALTER TABLE person_table
    """)


    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address;
    # """)

    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN address
    # """)

    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT NOT NULL DEFAULT "city, street"
    # """)

    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)


    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT "+79234557896100",
    # age INTEGER CHECK (age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )""")


