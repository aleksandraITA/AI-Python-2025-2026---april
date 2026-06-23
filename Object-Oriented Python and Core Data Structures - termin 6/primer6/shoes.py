from product import Product

class Shoes(Product):
    
    def tax(self):
        return self.price * 1.2
    
    