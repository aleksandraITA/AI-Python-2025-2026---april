# Na osnovu liste transakcija, 
# napravi novu listu koja sadrži samo one 
# transakcije koje su veće od 100 000.

transactions = [45000, 120000, 250000, 80000, 130000]
large_transactions = []

for t in transactions:
    if t > 100000:
        large_transactions.append(t)

print(large_transactions)