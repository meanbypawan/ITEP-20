def calculation(f1,f2,f3):
    a = int(input("Enter 1st number.."))
    b = int(input("Enter 2nd number..."))
    result = f1(a,b)
    print(f"Addition  : {result}")
    result = f2(a,b)
    print(f"Subtraction : {result}")
    result = f3(a,b)
    print(f"Multiplication : {result}")

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

calculation(add,sub,mult)