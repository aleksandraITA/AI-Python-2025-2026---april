orders = [
(101, "John Doe", 299.99, "Pending"),
(102, "Jane Smith", 149.50, "Shipped"),
(103, "Mike Johnson", 89.75, "Delivered"),
(104, "Emily Davis", 249.99, "Pending"),
]

# order = tuple()

for order in orders:
    id, name, price, status = order
    
    #id = order[0]
    #name = order[1]
    #price = order[2]
    #status = order [3]
    
    if status == "Pending":
        print(id, name, price)