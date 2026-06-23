x = int(input("Unesite prvi broj: "))
y = int(input("Unesite drugi broj: "))
z = int(input("Unesite treci broj: "))

if x >= y and x >= z:
    print(f"Najveci broj je {x}")
    
if y >= x and y >= z:
    print(f"Najveci broj je {y}")
    
if z >= x and z >= y:
    print(f"Najveci broj je {z}")

