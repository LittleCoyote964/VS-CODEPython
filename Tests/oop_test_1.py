# -*- coding: utf-8 -*-
"""OOP_TEST_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vefVXeW6jT65hmxK8uV6ha9Sr668tMk9
"""

class Car:
    def __init__(self, brand, model, year, mileage, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage} miles, Price: ${self.price}")

    def update_price(self, new_price):
        self.price = new_price
        print(f"Updated Price of the {self.model}: ${self.price}")

class Sedan(Car):
    def __init__(self, brand, model, year, mileage, price, mpg, comfort_level):
        super().__init__(brand, model, year, mileage, price)
        self.mpg = mpg
        self.comfort_level = comfort_level

class SUV(Car):
    def __init__(self, brand, model, year, mileage, price, four_wheel_drive, off_road_capability):
        super().__init__(brand, model, year, mileage, price)
        self.four_wheel_drive = four_wheel_drive
        self.off_road_capability = off_road_capability

class Truck(Car):
    def __init__(self, brand, model, year, mileage, price, max_load, trailer_hitch):
        super().__init__(brand, model, year, mileage, price)
        self.max_load = max_load
        self.trailer_hitch = trailer_hitch

# Creating instances
my_sedan = Sedan('Toyota', 'Camry', 2020, 15000, 22000, 33, 'High')
my_suv = SUV('Jeep', 'Cherokee', 2022, 10000, 35000, True, True)
my_truck = Truck('Ford', 'F-150', 2019, 45000, 27000, 7500, True)

# Displaying vehicle information
my_sedan.display_info()
my_suv.display_info()
my_truck.display_info()

# Updating vehicle prices
my_sedan.update_price(21000)
my_suv.update_price(34000)
my_truck.update_price(26000)