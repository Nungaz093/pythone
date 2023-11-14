class CarClass:
    def __init__(self, brand, model, year, km):
        self.brand = brand
        self.model = model
        self.year = year
        self.km = km

    def info(self):
        print(f"{self.brand}, {self.model}, {self.year}год,{self.km} км")
