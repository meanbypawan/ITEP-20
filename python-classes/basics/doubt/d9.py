def division_decorator(func):
    def wrapper(a,b):
       if b == 0:
           print("Denominator can't be zero..")
           return None    
       result = func(a,b)
       return result
    
    return wrapper

@division_decorator
def division(a,b):
    return a / b

result = division(2,0)
print(f"Result : {result}")