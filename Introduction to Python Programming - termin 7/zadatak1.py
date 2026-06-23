def izracunaj_prosek(scores):
    '''
    suma = 0
    for el in scores:
        suma += el
    '''
    if len(scores) == 0:
        return None
    else:
        suma = sum(scores) 
        brElemenata = len(scores)
        prosek = suma / brElemenata
        return prosek


ocene = [ 5, 3, 4, 5, 5, 4, 5, 2, 5]
result = izracunaj_prosek(ocene)
print(result)

    
    