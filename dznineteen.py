class Account:
    rate_usd = 0.013
    rate_eu = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eu = 'EUR'

    def __init__(self, surname, number, procent, summarub):
        self.surname = surname
        self.__number = number
        self.procent = procent
        self.summarub = summarub
        print(f"Счет №{self.number} Принадлежащий {self.surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет №{self.number} Принадлежащий {self.surname} был закрыт.")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        self.__number = val

    @staticmethod
    def convert(summarub, rate):
        return summarub * rate

    @classmethod
    def set_usr_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_uer_rate(cls, rate):
        cls.rate_eu = rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.summarub, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eu(self):
        eu_val = Account.convert(self.summarub, Account.rate_eu)
        print(f'Состояние счета: {eu_val} {Account.suffix_eu}')

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.summarub += self.summarub * self.procent
        print("Проценты были успешно начислены!")
        self.print_balans()

    def withdraw_money(self, val):
        if val > self.summarub:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.summarub -= val
            print(f"{val} {Account.suffix} было успешно снято!")
        self.print_balans()

    def add_money(self, val):
        self.summarub += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balans()

    def print_balans(self):
        print(f"Текущий баланс {self.summarub} {Account.suffix}")

    def print_info(self):
        print(f"Информация о счете:")
        print("-" * 20)
        print(f"№{self.number}")
        print(f"Владелец:{self.surname}")
        self.print_balans()
        print(f"Проценты: {self.procent:.0%}")
        print("-" * 20)


acc = Account("Долгих", '12345', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eu()
print()
Account.set_usr_rate(2)
acc.convert_to_usd()
Account.set_uer_rate(3)
acc.convert_to_eu()
print()
acc.edit_owner("Дюма")
acc.print_info()
acc.add_percent()
print()
acc.withdraw_money(3000)
print()
acc.withdraw_money(100)
print()
acc.add_money(5000)
acc.withdraw_money(3000)
print()


# class Account:
#     rate_usd = 0.013
#     rate_eu = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eu = 'EUR'
#
#     def __init__(self, surname, number, procent, summarub):
#         self.surname = surname
#         self.__number = number
#         self.procent = procent
#         self.summarub = summarub
#         print(f"Счет №{self.number} Принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет №{self.number} Принадлежащий {self.surname} был закрыт.")
#
#     @property
#     def number(self):
#         return self.__number
#
#     @number.setter
#     def number(self, val):
#         self.__number = val
#
#     @staticmethod
#     def convert(summarub, rate):
#         return summarub * rate
#
#     @classmethod
#     def set_usr_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_uer_rate(cls, rate):
#         cls.rate_eu = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.summarub, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eu(self):
#         eu_val = Account.convert(self.summarub, Account.rate_eu)
#         print(f'Состояние счета: {eu_val} {Account.suffix_eu}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.summarub += self.summarub * self.procent
#         print("Проценты были успешно начислены!")
#         self.print_balans()
#
#     def withdraw_money(self, val):
#         if val > self.summarub:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.summarub -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balans()
#
#     def add_money(self, val):
#         self.summarub += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balans()
#
#     def print_balans(self):
#         print(f"Текущий баланс {self.summarub} {Account.suffix}")
#
#     def print_info(self):
#         print(f"Информация о счете:")
#         print("-" * 20)
#         print(f"№{self.number}")
#         print(f"Владелец:{self.surname}")
#         self.print_balans()
#         print(f"Проценты: {self.procent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eu()
# print()
# Account.set_usr_rate(2)
# acc.convert_to_usd()
# Account.set_uer_rate(3)
# acc.convert_to_eu()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percent()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# acc.withdraw_money(3000)
# print()