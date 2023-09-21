a = 12
b = 4

a = a + b
b = a - b
a = a - b
print(a)
print(b)

a = a * b
b = a / b
a = a / b
print(a)
print(b)

a, b = b, a
print(a)
print(b)