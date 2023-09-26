def sr_a(fn):
    def wrap(*f_args):
        x = fn(*f_args)
        print('Среднее арифметическое чисел', end=' ')
        print(*f_args, sep=', ', end=' ')
        print('=', x / len(f_args))

    return wrap


@sr_a
def summa(*args):
    a = ""
    for i in args:
        a += str(i) + ", "
    print('Сумма чисел:', a[:-2], "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)
