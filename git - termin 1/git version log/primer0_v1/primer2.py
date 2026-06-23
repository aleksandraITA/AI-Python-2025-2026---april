prodaja= int(input('Unesite broj prodatih jedinica: '))
if prodaja > 100:
    print('Veoma uspešno!')
# elif 50 <= prodaja <= 100:
# elif prodaja <= 100 and 50 <= prodaja:
# elif prodaja >= 50 and prodaja <= 100 :
elif prodaja <= 100 and prodaja >= 50:
    print('Solidno, razmislite o akcijama.')
else:
    print('Slabo – pokrenite promocije.')