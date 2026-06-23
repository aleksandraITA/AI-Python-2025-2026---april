products = ["Laptop", "Phone", "Camera", "TV", "Headphones", "Camera"]
product = input("Unesite proiyvod koji trazimo: ")

nadjen = False

for i in range(len(products)):
    if product == products[i]:
        print(product, "is available on position:", i)
        nadjen = True
        break


if nadjen == False: 
    print(product," is not available.")