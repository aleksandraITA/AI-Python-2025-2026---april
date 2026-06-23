sizes = ["S", "M", "L"]
colors = ["Black", "Blue", "Red"]

for s in sizes:
    for c in colors:
        #print(s, "-", c)
        print(f"{s} - {c}")
        
print("--------------------")

for c in colors:
    for s in sizes:
        #print(s, "-", c)
        print(f"{s} - {c}")