# Data-Encapsulation
# Global pollutation

counter = 100

def increment():
    global counter
    counter += 1
    print(f"Inside increment {counter}")

def decrement():
    global counter
    counter -= 1
    print(f"Inside decrement {counter}")    