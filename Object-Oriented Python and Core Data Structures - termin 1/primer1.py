products = ["Laptop", "Mouse", "TV", "Monitor", "Microphone"]

# koristeći for petlju ispišite sve elemente liste
for i in products:
    print(i)

print("--------------------")

duzinaListe = len(products)
for i in range(duzinaListe):
    print(i, ":", products[i])
    
print("--------------------")  

# ispisi elemente liste u nazad
for i in range(duzinaListe-1, -1, -1):
    print(i, ":", products[i])    