a = 5
b = 0

try:
    x = a / b
except NameError:
    print("You won't see me!")
except ZeroDivisionError:
    print("Hey, you can't divide by zero!")
except Exception:
    print("I'm here just in case you didn't find anything")