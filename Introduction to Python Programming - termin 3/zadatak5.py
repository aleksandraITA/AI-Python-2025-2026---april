x = int(input("unesite prvi operand: "))
y = int(input("unesite drugi operand: "))

operacija = input("Unesite operaciju: ")
if operacija == "+":
    res = x + y
    print(res)
elif operacija == "-":
    print(x - y)
elif operacija == "*":
    print(x * y)
elif operacija == "/":
    if y != 0 :
        #res = x / y
        print(x/y)
    else:
        print("Nema deljenja nulom.")
else:
    print("Nevalidna operacija")