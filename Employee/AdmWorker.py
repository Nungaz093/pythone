from Employee import Emp


class AdmWorker(Emp.Employee):
    def __init__(self, name, surname, code, salary):
        super().__init__(name, surname, code)
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def month_salary(self):
        return round((self._salary / 7) * 30, 0)

    def info(self):
        print(f'Заработная плата: {self._code} - {self._name} {self._surname}\n'
              f'- Проверить сумму: {self.month_salary()}')