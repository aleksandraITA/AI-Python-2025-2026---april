def divide(a,b):
    if b ==0:
        return 0
    if a > 10 or b > 10:
        raise ArithmeticError("Number is larger than 10")
    else:
        return a/b
  
  
try:  
    print(divide(14,2))
except ArithmeticError:
    # b = 10
    print("Brojevi moraju biti manji od 10.")