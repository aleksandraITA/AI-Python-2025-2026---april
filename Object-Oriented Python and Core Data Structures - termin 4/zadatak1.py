class Product:
    naziv = ""
    cijena = 0.0
    kolicina = 0
        
product1 = Product()
product2 = Product()

product1.naziv = "Laptop"
product1.cijena = 1200.99
product1.kolicina = 5

product2.naziv = "Smartphone"
product2.cijena = 699.5
product2.kolicina = 10

print(f"produkt 1: naziv {product1.naziv}, cijena : {product1.cijena}, kolicina : {product1.kolicina}")
print(f"produkt 2: naziv {product2.naziv}, cijena : {product2.cijena}, kolicina : {product2.kolicina}")