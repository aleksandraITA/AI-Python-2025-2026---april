import sys


# Učitava podatke o putniku:
# pol putnika(na primer kao jedan karakter:'M' za muški ili'Ž' za ženski pol)
pol = input("Unesite pol (M ili Z): ").upper()
'''if  pol!='M' and pol!='Z':
    print("Niste uneli ocekivanu vrednost za pol.")
    sys.exit(1)
 '''   
# godine starosti putnika(ceo broj).
godine = int(input("Unesite godine: "))

# Ime i prezime putnika
imePrezime = input("Unesite ime i prezime: ")


''' 
if pol=='M' or pol=='Z':
    # radi dalje analize
    print("-")
else:
    print("Niste uneli ocekivanu vrednost za pol.")
    
    
if not(pol=='M' or pol=='Z'):
    print("Niste uneli ocekivanu vrednost za pol.")
else:
    # radi dalje analize
    print("-") 
    
# not(p or q) === not p and not q  
'''
titula = ""
if pol == 'Z':
    if godine < 18:
        titula = "Gospodjica"
        #print (f"Gospodjica {imePrezime}")
    else:
        titula = "Gospodja"
elif pol == 'M':
    if godine < 18:
        titula = "Mladi gospodin"
    else:
        titula = "Gospodin"     
else:
    print("Niste uneli ocekivanu vrednost za pol.")
    sys.exit(1)
    
print(f"{titula} {imePrezime}")
   


 

 
   