from random import  randint
n1 = int(input("Размер первого списка: "))
n2 = int(input("Размер второго списка: "))
a = [randint(0, 10) for i in range(n1)]
b = [randint(0, 10) for j in range(n2)]
print("Первый список: ", a)
print("Второй список: ", b)
s = a + b
print("Третий список: ", s)

s = []
for i in b:
    if i not in s:
        s.append(i)
print("Элементы обоих списков без повторений: ", s)

y = []
for i in a:
    for j in b:
        if i == j and i not in y:
            y.append(i)
if len(y) == 0:
    print("Без повтора: ")
else:
    print("Элемент общий для 2-х списков: ", y)

g = [a[0], b[0], a[-1], b[-1]]
g.sort()
print("Max and Min", g)
