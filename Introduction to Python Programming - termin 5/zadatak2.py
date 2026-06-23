brPokusaja = 0

while True:
    password = input("Unesite password: ")
    brPokusaja += 1
    #if password.lower() == "admin":
    if password == "admin":
        print("Logovanje uspesno")
        break
    else:
        print("Logovanje nije uspesno.")
        
    if brPokusaja == 3:
        print("Nalog zakljucan.")
        break
    