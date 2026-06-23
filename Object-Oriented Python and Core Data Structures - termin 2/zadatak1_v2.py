orders= [
(101, "Mina", 299.99, "Pending"),
(102, "Stefan", 149.50, "Shipped"),
(103, "Ivana", 89.75, "Delivered"),
(104, "Milan", 249.99, "Pending"),
(105, "Sara", 120.00, "Shipped"),
]

total = 0

for order in orders:
    order_id, customer, amount, status = order
    if status == "Pending":
        print(order_id, customer, amount)
    elif status == "Shipped" or status == "Delivered":
        total += amount    
print(total)