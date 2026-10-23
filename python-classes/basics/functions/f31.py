def test_decorator(func):  # closoure-cell func --> say_hello()
    def wrapper():
        print("Before...")
        func()
        print("After...")

    return wrapper

@test_decorator
def say_hello():
    print("Hello...")

say_hello()
# say_hello = test_decorator(say_hello) # say_hello --> wrapper
# say_hello()