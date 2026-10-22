counter = 100

def increment():
    global counter
    counter = counter + 1

def decrement():
    global counter
    counter = counter - 1

def display_counter():
    print(f"Counter : {counter}")

increment()
display_counter()
increment()
display_counter()
decrement()
display_counter()
decrement()
display_counter()
