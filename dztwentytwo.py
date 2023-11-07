class Student:
    def __init__(self, name):
        self.name = name
        self.na = self.CPU()

    def show(self):
        print(f"{self.name}", end=" ")
        self.na.show()

    class CPU:
        def __init__(self):
            self.hp = "HP"
            self.cor = "i7"
            self.pam = "16"

        def show(self):
            print(f"=> {self.hp}, {self.cor},{self.pam}")


s = Student("Roman")
s.show()
s2 = Student("Vadim")
s2.show()
