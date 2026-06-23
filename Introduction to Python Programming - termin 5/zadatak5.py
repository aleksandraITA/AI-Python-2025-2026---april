mesecniDataLimit = int(input("unesite mesecni data limit (u GB): "))
ukupnoPotrosena = 0
dan = 1

while dan <= 30:
    dnevnaPotrosnja = int(input(f"unesite potrosnju (u GB) za {dan}. dan: "))
    ukupnoPotrosena += dnevnaPotrosnja
    
    if ukupnoPotrosena >= mesecniDataLimit:
        print(f"Potrosili ste paket za {dan} dana.")
        break
    
    dan += 1
    

if dan > 30:
    print(f"Preostalo vam je {mesecniDataLimit-ukupnoPotrosena} na kraju meseca.")