def broj_reci(tekst):
    reci = tekst.split(" ")
    # ['Ovo', 'je', 'neki', 'tekst.']
    return len(reci)
    
    
result = broj_reci("Ovo je neki tekst.")
print(f"Vasa recenica ima {result} reci.")