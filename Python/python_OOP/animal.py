class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = 100


    def walk(self, x):
        self.health -= 1 * x
        return self

    def run(self, x):
        self.health -= 5 * x
        return self

    def displayHealth(self):
        if self.health <= 0:
            self.health = "You're dead."
        return 'Name: {}''\n''Health: {}'.format(self.name, self.health)

animal1 = Animal('Animal_1', 0)
print(animal1.walk(12).run(20).displayHealth())
print('-'*50)

class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150
    def pet(self, x):
        self.health += 5 * x
        return self

dog1 = Dog('Dog_1', 0)
print(dog1.walk(3).run(2).pet(1).displayHealth())
print('-'*50)

class Dragon(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 170
    def fly(self, x):
        self.health -= 10 * x
        return self

dragon1 = Dragon('Dragon_1', 0)
print(dragon1.displayHealth())
print("I am a Dragon")
print('-'*50)

animal3 = Animal('Animal_3', 0)
print(animal3.displayHealth())

