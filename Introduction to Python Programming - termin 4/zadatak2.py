tipKartice = input("Unesite tip kartice (Visa, Master): ").lower()
statusKupca = input("Unesite status kupca (Vip, Standard): ").lower()
iznos = int(input("Unesite iznos racuna: "))


if tipKartice == "visa":
    if statusKupca == "vip":
        print(iznos - iznos*0.07)
    elif statusKupca == "standard":
        print(iznos - iznos*0.03)
    else:
        print("Niste uneli ocekivanu vrednost za status kartice.")
elif tipKartice == "master":
    if statusKupca == "vip":
        print(iznos - iznos*0.05)
    elif statusKupca == "standard":
        print(iznos - iznos*0.02)
    else:
        print("Niste uneli ocekivanu vrednost za status kartice.")
else:
    print("Niste uneli ocekivanu vrednost za tip kartice.")