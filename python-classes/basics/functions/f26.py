def DataEncapsulation():
    counter = 100
    def increment():
        nonlocal counter
        counter = counter + 1

    def decrement():
        nonlocal counter
        counter = counter - 1

    def display_counter():
        print(f"Counter : {counter}")
    
    return increment,decrement,display_counter 

increment,decrement,display_counter = DataEncapsulation() 

increment()
display_counter()

decrement()
display_counter()

