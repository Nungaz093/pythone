from Employee import AdmWorker


class Worker(AdmWorker.AdmWorker):
    def month_salary(self):
        return self._salary * 8 * 22
