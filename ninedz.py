stud = []
ball = []
try:
    for i in range(int(input('Кол-во студентов: '))):
        stud.append(input(f'{i + 1}-й студент: '))
        ball.append(int(input('баллов: ')))
    all_b = dict(zip(stud, ball))

    res = 0
    for i in ball:
        res += i

    res = res / len(ball)
    print("Средний бал:", round(res), ".Студенты с баллом выше среднего: ")
    for s, z in all_b.items():
        if z > res:
            print(s)
except ValueError:
    print("Ошибка")
