# Zadatak: Dodavanje elemenata u listu

# Kreirati program koji omogućava korisniku da dodaje proizvode u listu.

# Potrebno je:
# 1. Kreirati praznu listu products
# 2. Od korisnika tražiti da unese 5 proizvoda
# 3. Svaki proizvod dodati u listu pomoću append() funkcije
# 4. Na kraju ispisati sve proizvode iz liste

products = []
for i in range (5):
    product = input ("Unesite svoj proizvod: ")
    products.append(product)
print (products)