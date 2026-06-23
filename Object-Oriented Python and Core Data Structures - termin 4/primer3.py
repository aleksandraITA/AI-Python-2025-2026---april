class Product:
    name =""
    price = 0.0
    quantity = 0
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"[name {self.name}, price : {self.price},  quantity : {self.quantity}]"
    
    def displayInfo(self):
        return f"Product: {self.name}, Price: {self.price} euros, Quantity: {self.quantity}"        


product1 = Product("Laptop", 700, 10)
product2 = Product("Mouse", 50, 85)
product3 = Product("Monitor", 150, 5)

print(product1.displayInfo())
print(product1)
