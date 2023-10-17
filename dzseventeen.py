class Automobile:
    def __init__(self, name, year, manufacture, power, color, price):
        self.name = name
        self.year = year
        self.manufacture = manufacture
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(42, *"*"))
        print(f"Название модели: {self.name}\nГод выпуска: {self.year}\nПроизводитель:{self.manufacture}"
              f"\nМощность двигателя: {self.power}"f"\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def set_auto(self, name, year, manufacture, power, color, price):
        self.name = name
        self.year = year
        self.manufacture = manufacture
        self.power = power
        self.color = color
        self.price = price

    def get_auto(self):
        return self.name, self.year, self.manufacture, self.power, self.color, self.price

    # def set_name(self, name):
    #     self.name = name
    #
    # def get_name(self):
    #     return self.name


a1 = Automobile("X7 M50i", "2021", "BMW", "530 l.s", "white", "10790000")
a1.print_info()

a1.set_auto("Honda", "2016", "Japan", "690 l.s", "red", "10990000")
a1.print_info()
print(a1.get_auto())

# a1.set_name("BMW-ZTX")
# a1.print_info()
# print(a1.get_auto())
