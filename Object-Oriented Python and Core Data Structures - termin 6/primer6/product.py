import abc

class Product(abc.ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @abc.abstractmethod
    def tax(self):
        pass


#p = Product("tv", 15000)
#p.tax()