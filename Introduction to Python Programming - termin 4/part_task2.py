kupci_ponedeljak = int(input ("broj kupaca je: "))
kupci_utorak = int(input("broj kupaca je: "))
kupci_sreda = int(input("broj kupaca je: "))
kupci_cetvrtak = int(input("broj kupaca je: "))
kupci_petak = int(input("broj kupaca je: "))
kupci_subota = int(input("broj kupaca je: "))
kupci_nedelja = int(input("broj kupaca je: "))

#prikaže ukupan broj kupaca za radne dane (ponedeljak–petak);
ukupno_kupaca_radni_dani = kupci_ponedeljak + kupci_utorak + kupci_sreda + kupci_cetvrtak + kupci_petak
#prikaže ukupan broj kupaca za vikend (subota i nedelja);
ukupno_kupaca_vikend = kupci_subota + kupci_nedelja
#izračuna i prikaže ukupan broj kupaca za celu nedelju;
ukupno_kupaca_nedelja = ukupno_kupaca_radni_dani + ukupno_kupaca_vikend

# da li je broj kupaca bio veci u nedelju ili subotu
if kupci_nedelja > kupci_subota :
    print(" prodaja je veca u nedelju ")
else:
    print(" prodaja je veca u subotu ")

# da li je prodaja tokom radnih dana bila veca od dana vikenda
if ukupno_kupaca_radni_dani > ukupno_kupaca_vikend:
    print(" prodaja veca za vikend ")
else:
    print(" prodaja veca za radne dane ")
    