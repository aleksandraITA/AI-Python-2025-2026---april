try:
    x = 100
    y = 0
    print(x/y)
except NameError:
    print("You won't see me!")
except ZeroDivisionError:
    print("Hey, you can't divide by zero!")
except Exception:
    print("I'm here just in case you didn't find anything")
finally:
    print("Value of y is: ",y)