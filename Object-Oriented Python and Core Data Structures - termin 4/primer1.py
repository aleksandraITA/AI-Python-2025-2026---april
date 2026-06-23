# Element	    ->  Stil
# Klase	        ->  PascalCase
# Metode	    ->  camelCase
# Promenljive   ->	camelCase
# Konstante	    ->  UPPER_CASE

class Product:
    name = ""
    price = 0.0
    quantity = 0
    
product1 = Product()
product2 = Product()

print("product1: ", product1)
print("product2: ", product2)

print(type(product1))

product1.name = "patike"
product1.price = 110
product1.quantity = 9

print(product1.name)


