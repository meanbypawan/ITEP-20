import time
def test_decorator(func):
    def wrapper():
        start = time.perf_counter() # performance_counter
        func()
        end = time.perf_counter()
        print(f"Execution Time : {end-start}")
    return wrapper


@test_decorator
def calculation_10000():
    total = sum(range(10000))
    print("10000 Calculation Done")

@test_decorator
def calculation_100000():
    total = sum(range(100000))
    print("100000 Calculation Done")    

calculation_10000()
calculation_100000()    