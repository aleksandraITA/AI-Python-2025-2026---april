# Maksimalan broj kupona i vreme trajanja promocije
maks_kupona = 100
vreme_trajanja = 7
# Trenutni status
iskorisceni_kuponi = 0

while iskorisceni_kuponi < maks_kupona and vreme_trajanja > 0:
    iskorisceni_kuponi += int(input("unesite broj iskoriscenih kupona danas: "))
    vreme_trajanja -=  1
    # Dodatni uslov za upozorenje
    if maks_kupona - iskorisceni_kuponi < 5:
        print("Upozorenje: Ostalo je manje od 5 kupona!")
        print(f"Istoršeno kupona: {iskorisceni_kuponi}")
        
print("Promocija je završena.")