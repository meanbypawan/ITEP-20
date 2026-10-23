def square_decorator(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return wrapper

@square_decorator
def add(a,b,c):
    return a+b+c

# add = square_decorator(add) # phase - 1 func --> add
# result = add(20,10) # wrapper
result = add(2,4,3)
print(f"Result : {result}")