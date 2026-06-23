sales = {
    "Laptop": (15,1200),
    "Phone": (28, 800),
    "Tablet": (10,500),
    "Monitor": (7,300),
    "Headphones": (20, 150)
}


# izracunaj ukupnu vrednost prodaje
total = 0
for key in sales.keys():
    total += sales[key][0] * sales[key][1]
    
print(total)

