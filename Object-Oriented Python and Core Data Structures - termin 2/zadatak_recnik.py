sales = {
    "Laptop": 15,
    "Phone": 28,
    "Tablet": 10,
    "Monitor": 7,
    "Headphones": 20
}

prices = {
    "Laptop": 1200,
    "Phone": 800,
    "Tablet": 500,
    "Monitor": 300,
    "Headphones": 150
}

# izracunaj ukupnu vrednost prodaje
total = 0
for key in prices.keys():
    total += sales[key] * prices[key]
    
print(total)


# najprodavaniji proizvod
best_product = max(sales, key = sales.get)
print(best_product)