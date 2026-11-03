def DataEncapsulation():
    counter = 100
    def increment():
        nonlocal counter
        counter = counter + 1
        print(f"counter increment: {counter}")
    
    def decrement():
        nonlocal counter
        counter = counter - 1
        print(f"counter decrement : {counter}")

    return increment,decrement

increment,decrement = DataEncapsulation()
increment()
increment()
decrement()
decrement()