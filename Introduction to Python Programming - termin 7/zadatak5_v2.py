def ukupna_cena(cene):
    return sum(cene)

def najskuplji_proizvod(nazivi, cene):
    max_cena = max(cene)
    indeks = cene.index(max_cena)
    return nazivi[indeks], cene[indeks]
    
cene = [ 100, 150, 200, 120, 85]
nazivi = ["Hleb", "Mleko", "Sir", "Jaja", "Jogurt"]
naziv, cena = najskuplji_proizvod(nazivi, cene)
print(f"Najskuplji proizvod je {naziv} i kosta {cena} dinara.")

