class Calculator:
    a = 0
    b = 0
    
    def add(self):
        return(self.a + self.b)
    def sub(self):
        return(self.a - self.b)
    def mul(self):
        return(self.a * self.b)
    def div(self):
        return(self.a % self.b)


rijesenje1 = Calculator()
rijesenje1.a = 5
rijesenje1.b = 10

print(rijesenje1.add())
print(rijesenje1.sub())

rijesenje1.a = 15
rijesenje1.b = 2


print(rijesenje1.mul())
print(rijesenje1.div())