max = 0

while True:
    unos = input("Unesite broj: ")
    if unos == "STOP":
        print(f"Najveci uneti broj je : {max}")
        break
    else:
        broj = int(unos)
        if broj > max:
            max = broj