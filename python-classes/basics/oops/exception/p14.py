def m1():
    try:
        a = int(input("Enter 1st value.."))
        b = int(input("Enter 2nd value..."))
        c = a / b
        print(f"Result : {c}")
        #return 100 
    except ZeroDivisionError as e:
        print("ZeroDivsionError Caught..")    

    except:
        print("Unknown Exception Caught...")

    else:
        print("Else Block Executed | There is no exception in code..")
        return 100
    finally:
        print("Finally Block Execute...")    
        return 200
print(m1())