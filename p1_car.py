from datetime import datetime

class Car:
    no_of_cars = 0
    wheels = 4

    @staticmethod
    def display_wheels():
        return f"The car has {Car.wheels} wheels"

    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        Car.no_of_cars += 1

    def display_info(self):
        print(f"Car:{self.color} {self.brand} {self.model} ({self.year})")

    def age(self):
        today = datetime.now().year
        age = today - self.year
        return age
    
    def is_vintage(self):
        age = self.age()
        if age > 25:
            return True
        else:
            return False
        
    def __str__(self):
        return f"""______________CAR PROFILE___________
Brand: {self.brand}
MODEL: {self.model}
YEAR: {self.year}
COLOR: {self.color}
PRICE: UGX. {self.price}
VINTAGE: {self.is_vintage()}"""
    
    def compare_year(self, car_obj):
        my_age = self.age()
        other_age = car_obj.age()

        if my_age < other_age:
            return f"My {self.brand} {self.model} is NEWER than your {car_obj.brand} {car_obj.model}"
        elif my_age > other_age:
            return f"Your {car_obj.brand} {car_obj.model} is NEWER than my {self.brand} {self.model}"
        else:
            return "Both our cars are the SAME AGE"
        
    




car1 = Car("Toyota", "LandCruiser", 2009, "Blue", 120000)
car2 = Car("Subaru", "BRZ", 2021,"Grey", 190000)

print(Car.no_of_cars)
print(car1.compare_year(car2))
print(Car.display_wheels())