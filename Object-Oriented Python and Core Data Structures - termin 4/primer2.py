class Product:
    name =""
    price = 0.0
    quantity = 0
    
    # Define a method for applying a discount
    def getDiscountedPrice(self, procenat):
        return self.price * (100 - procenat) / 100
    
product1 = Product()
product2 = Product()

product1.price = 100
product2.price = 150

print(f"product1: {product1.price}")
print(f"product2: {product2.price}")

print(product1.getDiscountedPrice(10))
print(product2.getDiscountedPrice(50))