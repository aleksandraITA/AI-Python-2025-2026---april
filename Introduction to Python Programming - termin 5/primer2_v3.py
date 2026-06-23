# Maksimalan broj kupona i vreme trajanja promocije
dostupni_kuponi = 100
vreme_trajanja = 7
# Trenutni status
broj_dana = 1

while broj_dana <= vreme_trajanja:
    dostupni_kuponi -= int(input(f"unesite broj iskoriscenih kupona nakon {broj_dana}.dana: "))
    broj_dana += 1
    # Dodatni uslov za upozorenje
    if dostupni_kuponi <= 5:
        print("Upozorenje: Ostalo je manje od 5 kupona!")
        print(f"Preostalo kupona: {dostupni_kuponi}")
    if dostupni_kuponi <= 0:
        print("Zavrsavamo akciju jer nemamo vise kupona.")
        break
        
print("Promocija je završena.")