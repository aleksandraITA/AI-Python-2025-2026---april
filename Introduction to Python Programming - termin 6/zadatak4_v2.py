ocene = [5, 4, 5, 5, 2, 4, 1]

# nadji prosek ocena
n = len(ocene)
suma = 0
for ocena in ocene:
    suma += ocena
prosek = suma / n
print(f"Prosek je: {prosek}.")


# prebroj petice
petice = 0
for ocena in ocene:
    if ocena == 5:
        petice += 1
print(f"Najvisih ocena je {petice}")






