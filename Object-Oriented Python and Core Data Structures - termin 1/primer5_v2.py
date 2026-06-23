products = ["Laptop", "TV", "Phone", "TV", "Headphones", "Camera", "TV",]

print("pre uklanjanja: ", products, len(products))

product = "TV"
while product in products:
    products.remove(product)
    print("posle uklanjanja: ", products, len(products))

