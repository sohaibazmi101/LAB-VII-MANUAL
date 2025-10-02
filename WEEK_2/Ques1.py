class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Car: {self.make} {self.model}, Year: {self.year}")
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)
car1.display_info()
car2.display_info()