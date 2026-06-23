temp_avg = float(input("Temperatura: "))
rain_chance = int(input("Vjerovatnoca kise: "))
wind_speed = int(input("Brzina Vjetra je: "))
target_sport = input("Zeljeni sport").lower()

if rain_chance > 60:
    print("Vjezbanje u teretani")
else:
#   if 10 <= temp_avg <= 25:
    if temp_avg >= 10 and  temp_avg <= 25 :
        if wind_speed < 8:
            if target_sport == "trcanje":
                print("Idealno za trcanje napolju!")
            elif target_sport == "setnja":
                print("Idealno za setnju napolju!")
            else: 
                print("Sport nije jedan od ponudjenih")  
        else:
            print("Vetar je brz.")         
    elif temp_avg < 10:
        print("Prehladno je, preporuka: vjezbaj u teretani")
    else:
        print("prevruce je, biraj aktivnost, laganu setnju ili teretanu")