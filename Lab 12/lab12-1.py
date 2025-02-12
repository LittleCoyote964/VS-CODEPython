class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

class minivan(Car):
    def __init__(self, brand, model, year, hasASD):
        super().__init__(brand, model, year)
        self.hasASD = hasASD

    def display(self):
        super().display()
        print(f"Does it have sliding door?: {self.hasASD}")

m1 = minivan("Toyota", "Sienna", "2023", True)
m2 = minivan("Honda", "Odyssey", "2012", True)
m3 = minivan("Honda", "Civic", "2024", False)
m1.display()
m2.display()
m3.display()