products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
product = input("Unesite proiyvod koji trazimo: ")


if product in products:
    print(product, "is available on position:", products.index(product))
else:
    print(product," is not available.")
    
print(products)