cap = int(input('Введите число от 1 до 99: '))
if 1 <= cap <= 99:
    if 10 <= cap <= 19 or 5 <= cap % 10 <= 9:
        print('Ваш баланс:', cap, 'Копеек')
    elif cap % 10 == 1:
        print('Ваш баланс:', cap, 'Копейка')
    else:
        print('Ваш баланс:', cap, 'Копейки')
else:
    print('Мимо, надо от 1 до 99')