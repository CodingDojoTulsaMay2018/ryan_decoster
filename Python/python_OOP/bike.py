class Bike:
    def __init__ (self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        
    def displayInfo(self):
        return 'Price = ${}, ' 'Max Speed = {}, ' 'Total Miles = {}'.format(self.price, self.max_speed, self.miles)
    def ride(self, times):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self, times):
        if self.miles <= 0:
            print("Negative miles don't exist!")
            return self
        else:
            print("Reversing")
            self.miles -= 5
            return self

bike1 = Bike(200, "25mph", '')
bike2 = Bike(350, "30mph", '')
bike3 = Bike(150, "25mph", '')

print(bike1.ride(3).reverse(1).displayInfo())

print(bike2.ride(2).reverse(2).displayInfo())

print(bike3.reverse(3).displayInfo())

    
