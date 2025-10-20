class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")

car1 = Car("Toyota", "LandCruiser", 2021)
car2 = Car("Subaru", "BRZ", 2021)

car1.display_info()
car2.display_info()   