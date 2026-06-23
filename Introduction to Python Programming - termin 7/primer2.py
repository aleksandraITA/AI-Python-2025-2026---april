# # Definišemo funkciju za izračunavanje popusta 
# funkcija prima cenu i procenat popusta i ispisuje novu umanjene cenu
def racunaj_cenu_sa_popustom(cena, popust):
    novaCena = cena - cena * popust / 100
    return novaCena
    


cena = 100
popust = 15
result = racunaj_cenu_sa_popustom(cena,popust)
print(f"Nova cena: {result}")


print(racunaj_cenu_sa_popustom(200,50))