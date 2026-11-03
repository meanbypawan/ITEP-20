def test_decorator(func):
    def wrapper():
        print("Before..")
        func()
        print("After..")
    return wrapper

@test_decorator
def say_hello():
    print("Hello..")

@test_decorator
def say_bye():
    print("Bye..")

say_hello()        
say_bye()