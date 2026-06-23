kupci= ["Marko", "Ana", "Lena", "Tom", "Iva"]
lojalni_kupci = ["Ana", "Tom", "Iva"]


for kupac in kupci:
    if kupac not in lojalni_kupci:
        print(f"Poštovani {kupac}, imamo specijalnu ponudu za vas da postanete lojalni član!")