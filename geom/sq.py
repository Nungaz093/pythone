class Square:
    def __init__(self, a):
        self.a = a

    def get_perimetr(self):
        return self.a * 4


if __name__ == '__main__':
    s3 = Square(30)
    print(s3.get_perimetr())
