def ukupna_cena(cene):
    return sum(cene)

def najskuplji_proizvod(nazivi, cene):
    max_cena = cene[0]
    indeks = 0   
    for i in range(1,len(cene)):
        if cene[i]>max_cena:
            max_cena = cene[i]
            indeks = i
    return nazivi[indeks], cene[indeks]
    
cene = [ 100, 150, 200, 120, 85]
nazivi = ["Hleb", "Mleko", "Sir", "Jaja", "Jogurt"]
naziv, cena = najskuplji_proizvod(nazivi, cene)
print(f"Najskuplji proizvod je {naziv} i kosta {cena} dinara.")

