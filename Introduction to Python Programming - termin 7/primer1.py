def odluka_za_oblacenje(vreme):
    if vreme=="sunce":
        print("Poneseti naocare za sunce.")
    elif vreme=="kisa":
        print("Poneseti kisobran.")
    else:
        print("Oblacno je, ali ne morate nositi nista posebno.")
        
vreme = input("unesite vreme: ")
odluka_za_oblacenje(vreme)

''' sad ovde ide neki kod od desetak linija'''


odluka_za_oblacenje("oblacno")