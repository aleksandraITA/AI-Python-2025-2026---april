from product import Product

class Tehnika(Product):
    
    def tax(self):
        return self.price * 1.3