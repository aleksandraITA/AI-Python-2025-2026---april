order ={
"customer": "John Doe",
"product": "Laptop",
"price": 75000,
"date": "2024-10-15",
"status": "delivered"
}


for key, value in order.items():
    print(key, " - ", value)
    
print(order.get("price"))

print(order["price"])