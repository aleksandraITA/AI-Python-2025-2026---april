ocene = [5, 4, 5, 5, 2, 4, 1]

# nadji prosek ocena
n = len(ocene)
suma = 0
petice = 0
for ocena in ocene:
    suma += ocena
    if ocena == 5:
        petice += 1

prosek = suma / n
print(f"Prosek je: {prosek}.")

print(f"Najvisih ocena je {petice}")






