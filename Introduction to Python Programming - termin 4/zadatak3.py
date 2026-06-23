# visits_yesterday – broj poseta juče
visits_yesterday = int(input("Unesite broj poseta od juce: "))

# visits_today – broj poseta danas
visits_today = int(input("Unesite broj poseta danas: "))

# conversions_today – broj ljudi koji su danas kupili neki proizvod na sajtu
conversions_today = int(input("Broj ljudi koji je danas kupio kurs: "))

# target_visits – cilj za broj poseta(npr. 150)
target_visits = int(input("Koji je vas cilj u broju poseta: "))

if visits_today > visits_yesterday:
    if visits_today >= target_visits:
        print("Target ostvaren.")
    else:
        print("Target nije postignut")
else:
    print("Upozorenje: danas imamo manje ili isto poseta kao juče!")