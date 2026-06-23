def prebroj_poz_neg(brojevi):
    poz = 0
    neg = 0
    
    for broj in brojevi:
        if broj >= 0:
            poz+=1
        else:
            neg+=1
    
    return poz, neg 

brojevi = [1,-2,3,4,5,-6,7,8,-9]
result, result2  = prebroj_poz_neg(brojevi)
print("Pozitivni:", result)
print("Negativni:", result2)