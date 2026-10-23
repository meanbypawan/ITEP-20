def square_decorator(func):
    def wrapper(x,y):
        result = func(x*x, y*y)
        return result
    return wrapper

@square_decorator
def add(a,b):
    return a + b

# add = square_decorator(add) # phase - 1 func --> add
# result = add(20,10) # wrapper
result = add(2,4)
print(f"Result : {result}")