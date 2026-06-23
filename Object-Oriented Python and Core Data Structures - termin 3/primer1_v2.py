# Na osnovu liste transakcija, 
# koristeci lambda funkciju
# napravi novu listu koja sadrži samo one 
# transakcije koje su veće od 100 000.

transactions = [45000, 120000, 250000, 80000, 130000]
# ako lambda vrati True -> element ostaje
# ako lambda vrati False -> element se izbacuje
res = list(filter(lambda t: t > 100000, transactions))

# 45000   -> False -> izbacuje se
# 120000  -> True  -> ostaje
# 250000  -> True  -> ostaje
# 80000   -> False -> izbacuje se
# 130000  -> True  -> ostaje

print(res)