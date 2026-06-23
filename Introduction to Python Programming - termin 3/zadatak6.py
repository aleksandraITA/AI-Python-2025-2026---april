cena = int(input("Unesite cenu bez poreza: "))
drzava = input("Unesite drzavu: ")

if drzava == "RS":
    cenaSaPorezom = cena * 1.2
    #print(cenaSaPorezom)
elif drzava == "US" or drzava == "CA":
    cenaSaPorezom = cena * 1.13
    #print(cenaSaPorezom)
elif drzava == "EU":
    cenaSaPorezom = cena * 1.07
    #print(cenaSaPorezom) 
else:
    cenaSaPorezom = cena * 1.25
    #print(cenaSaPorezom) 

print(cenaSaPorezom)        