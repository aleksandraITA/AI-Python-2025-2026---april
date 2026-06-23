def izracunaj_uvecanu_cenu(cena, procenat):
    novaCena = cena  + cena * procenat / 100
    return novaCena



# pitati korisnika da vam unese NETO cenu
netoCena = float(input("Unesite NETO cenu: "))
# izracunaj bruto cenu
brutoCena = izracunaj_uvecanu_cenu(netoCena, 20)
#ispisi bruto cenu
print(brutoCena)