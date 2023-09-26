def func(a):
    r = ''
    while a > 0:
        r = str(a % 2) + r
        a = a // 2

    print(r)


while True:
    n = int(input("==> "))
    if n == 0:
        break
    func(n)
