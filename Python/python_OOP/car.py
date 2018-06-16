class Car:
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = mileage
        self.tax = 0.12
        if self.price > 10000:
            self.tax = 0.15
    
    def display_all(self):
        return 'Price: ${}''\n''Speed: {}''\n''Fuel: {}''\n''Mileage: {}''\n''Tax: {}''\n'.format(self.price, self.speed, self.fuel, self.milage, self.tax)
    
car1 = Car(2000, '35mph', 'Full', '15mpg', '')
car2 = Car(2000, '5mph', 'Not Full', '105mpg', '')
car3 = Car(2000, '15mph', 'Kind of Full', '95mpg', '')
car4 = Car(2000, '25mph', 'Full', '25mpg', '')
car5 = Car(2000, '45mph', 'Empty', '25mpg', '')
car6 = Car(20000000, '35mph', 'Empty', '15mpg', '')

print(car1.display_all())
print(car2.display_all())
print(car3.display_all())
print(car4.display_all())
print(car5.display_all())
print(car6.display_all())