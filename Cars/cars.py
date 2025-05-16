class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model}'s engine is running.")
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.year} {self.make} {self.model}'s engine is now stopped.")
        else:
            print("The engine is already stopped")

    def get_car_info(self):
        print(f"Make {self.make}")
        print(f"Model {self.model}")
        print(f"Year {self.year}")
        print(f"Engine Status: {'Running' if self.is_running else 'Stopped'}")


# Creating Car Objects
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

print(car1.make)
print(car2.year)

car1.start_engine()
car1.stop_engine()
car1.get_car_info()

car2.start_engine()
car2.start_engine()
car2.get_car_info()
car2.stop_engine()
