from Employee import AdmWorker


class Trader(AdmWorker.AdmWorker):
    def __init__(self, name, surname, code, salary, sell):
        super().__init__(name, surname, code, salary)
        self._sell = sell

    def get_sell(self):
        return self._sell

    def set_sell(self, sell):
        self._sell = sell

    def month_salary(self):
        return self._salary + self._sell * 0.05
