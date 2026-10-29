#            20,10, callback = add 
def operation(a,b,callback):
    print(f"a : {a}")
    print(f"b : {b}")
    result = callback(a,b)
    print(f"Result : {result}")

# def add(a,b):
#     return a + b

# def multiplication(a,b):
#     return a * b

operation(20,10,lambda a,b:a+b)    
operation(20,10,lambda a,b:a*b)