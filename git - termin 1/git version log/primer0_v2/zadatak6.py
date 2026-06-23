cena = int(input("Unesite cenu bez poreza: "))
drzava = input("Unesite drzavu: ")

if drzava == "RS":
    cenaSaPorezom = cena * 1.2
else:
    cenaSaPorezom = cena * 1.25
    #print(cenaSaPorezom) 

print(cenaSaPorezom)        