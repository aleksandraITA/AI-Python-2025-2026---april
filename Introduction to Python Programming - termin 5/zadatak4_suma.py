zbir = 0

while True:
    unos = input("Unesite broj: ")
    if unos == "STOP":
        print(f"Zbir unetih brojeva je: {zbir}")
        break
    else:
        zbir += int(unos)