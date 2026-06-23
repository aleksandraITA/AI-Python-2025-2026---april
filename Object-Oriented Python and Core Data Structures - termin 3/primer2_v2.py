# napravite listu brojeva od 1 do 100 sa korakom 3
# napravite novu listu koja ima samo parne brojeve iz prethodne liste
brojevi = list(range(1,100,3))
print(brojevi)
parni = [br for br in brojevi if br % 2 == 0]
print(parni)