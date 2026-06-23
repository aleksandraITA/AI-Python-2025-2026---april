prices = ["1200", "900", "", "450", None, "120", 45, 123, "45"]

sum = 0
br = 0
for p in prices:
    try:
        sum += int(p)
        br += 1
        print("Obradili smo ", p)
    except ValueError:
        print("imate prazan string")
        #sum += 0
    except TypeError:
        # sum += 0
        print("ne mozete na sumu dodati string")
        # pass


    
print(sum)