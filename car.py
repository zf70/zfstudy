class Car():
    def __init__(self,make,modle,year):
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 10000
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.modle
        return long_name.title()
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' mills on it.')
    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):                                #子类
    def __init__(self,make,modle,year):
        super().__init__(make,modle,year)
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

