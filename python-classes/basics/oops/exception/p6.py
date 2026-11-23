print("At the start...")
try:
    a = int(input("Enter 1st value..."))
    b = int(input("Enter 2nd value...."))
    c = a / b
    print(f"Result : {c}")
except ArithmeticError as e:
    print("ArithmeticError Caught...")
except ZeroDivisionError as e:
    print("ZeroDivisionError Caught...")
except ValueError as e:
    print("ValueError Caught...")            

print("At the end....")