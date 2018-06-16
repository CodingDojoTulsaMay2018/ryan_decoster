class Product:
    def __init__(self, price, name, weight, brand, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = 'For Sale'

    def displayInfo(self):
        return 'Price: ${}''\n''Name: {}''\n''Weight: {}''\n''Brand: {}''\n''Status: {}''\n'.format(self.price, self.name, self.weight, self.brand, self.status)
    
    def sell(self):
        self.status = 'Sold'
        return self

    def tax(self, tax):
        self.price = self.price + (self.price * tax)
        return self

    def returnItem(self, reason_for_return):
        if reason_for_return == 'defective':
            self.status = 'Defective'
            self.price = 0
            return self
        elif reason_for_return == 'like new':
            self.status = 'For Sale'
            return self
        elif reason_for_return == 'opened':
            self.status = 'Used'
            self.price = self.price - (self.price * 0.20)
            return self

product1 = Product(5, 'Bread', '1lb', 'Wonder', '')

print(product1.sell().tax(0.12).returnItem('opened').displayInfo())
    
    
