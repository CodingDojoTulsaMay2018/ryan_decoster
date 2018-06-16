class MathDojo:
    def __init__(self, name):
        self.name = name
        self.result = 0
    def add(self, *args):
        sum = 0
        for i in args:
            sum += i
        self.result += sum
        return self
    def subtract(self, *args):
        sum = 0
        for i in args:
            sum -= i
        self.result += sum
        return self
    
md = MathDojo('md')
md.add(2).add(2,5,1).subtract(3,2).result
print(md.result)