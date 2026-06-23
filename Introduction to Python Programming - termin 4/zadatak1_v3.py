# Učitava podatke o putniku:
# pol putnika(na primer kao jedan karakter:'M' za muški ili'Ž' za ženski pol)
pol = input("Unesite pol (M ili Z): ").upper()
# godine starosti putnika(ceo broj).
godine = int(input("Unesite godine: "))
# Ime i prezime putnika
imePrezime = input("Unesite ime i prezime: ")

if pol == 'Z'and godine < 18:
    print (f"Gospodjica {imePrezime}")
elif pol == 'Z'and godine >= 18:
    print (f"Gospodja {imePrezime}")
elif pol == 'M'and godine < 18:
    print (f"Mladi gospodin {imePrezime}")
elif pol == 'M'and godine >= 18:
    print (f"Gospodin {imePrezime}")
else:
    print("Niste uneli ocekivanu vrednost za pol.")
    
   


 

 
   