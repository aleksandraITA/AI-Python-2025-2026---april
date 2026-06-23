prices = [100, 250, 150, 300, 50, 200, 175, 80, 120, 275]
max_price = int(input("Max povoljna cena? "))

#napravite novu listu koja ima elemente manje od max_price

# resenje 1
filtered_prices = [price for price in prices if price <= max_price]
print(filtered_prices)

# resenje 2
prices_lower = []
for price in prices:
    if price <= max_price:
        prices_lower.append(price)
print(prices_lower)

# resenje 3
cene = list(filter(lambda price: price <= max_price, prices))
print(cene)
