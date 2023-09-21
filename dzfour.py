m = []
for i in range(int(input('n= '))):
    n = int(input('==>>'))
    if n == 0:
        continue
    m.append(n)
print(sum(m) / len(m))


# rad = int(input('Введите размер поля: '))
# sym = int(input('Введите количество символов: '))
#
# for i in range(rad):
#     for h in range(sym):
#         for j in range(rad):
#             for k in range(sym):
#                 if (i + j) % 2 == 0:
#                     print('*', end='')
#                 else:
#                     print(' ', end='')
#         print('')
