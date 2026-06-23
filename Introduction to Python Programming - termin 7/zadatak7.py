def broj_pojavljivanja(tekst, rec):
    tekst = tekst.lower()
    rec = rec.lower()
    reci = tekst.split(" ")
    return reci.count(rec)

tekst = input("Unesi tekst: ")
rec = input("Unesi reč koju tražiš: ")
broj = broj_pojavljivanja(tekst, rec)
print("Reč se pojavila", broj, "puta.")