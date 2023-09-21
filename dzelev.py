import math


def args_decor(fn):
    def wrap(*args, **kwargs):
        fn(*args, **kwargs)

    return wrap


@args_decor
def score(a, b, c, d):
    print(a + b + c + d)


score(2, 3, 3, 4)


@args_decor
def score1(a, b, c, d):
    let = len(str(score1))
    print(int(let)//(a + b + c + d))


score1(2, 3, 3, 4)


