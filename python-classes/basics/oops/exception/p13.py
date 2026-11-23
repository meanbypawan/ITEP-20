
try:
    a = int(input("Enter 1st value.."))
    b = int(input("Enter 2nd value..."))
    c = a / b
    print(f"Result : {c}")

except ZeroDivisionError as e:
    print("ZeroDivsionError Caught..")    

except:
    print("Unknown Exception Caught...")

else:
    print("Else Block Executed | There is no exception in code..")
    
finally:
    print("Finally Block Execute...")    