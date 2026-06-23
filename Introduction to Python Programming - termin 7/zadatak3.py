def validna_lozinka(password):
    if len(password)<8:
        return False 
    imaVeliko = False
    imaCifra = False
    for karakter in password:
        if karakter.isupper():
            imaVeliko = True
            break
    for karakter in password:
        if karakter.isdigit():
            imaCifra = True
            break
    '''if imaVeliko and imaCifra:   
        return True
    else:
        return False
    '''
    return imaVeliko and imaCifra
        

print(validna_lozinka("ab23bcabC"))        
    