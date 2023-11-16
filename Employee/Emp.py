class Employee:
    def __init__(self, name, surname, code):
        self._name = name
        self._surname = surname
        self._code = code

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_surname(self):
        return self._name

    def set_surname(self, surname):
        self._surname = surname

    def get_code(self):
        return self._code

    def set_code(self, code):
        self._code = code
