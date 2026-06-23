orders= [
(101, "Mina", 299.99, "Pending"),
(102, "Stefan", 149.50, "Shipped"),
(103, "Ivana", 89.75, "Delivered"),
(104, "Milan", 249.99, "Pending"),
(105, "Sara", 120.00, "Shipped"),
]

shipped_amount = 0
delieverd_amount = 0

for order in orders:
    order_id, customer, amount, status = order
    if status == "Pending":
        print(order_id, customer, amount)
    elif status == "Shipped":
        shipped_amount += amount
    elif status == "Delivered":
        delieverd_amount += amount

print("Shipped", shipped_amount)
print("Delivered", delieverd_amount)