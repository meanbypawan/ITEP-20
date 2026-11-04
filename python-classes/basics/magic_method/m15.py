class Test:
    
    def __new__(cls):
        print("__new__ called...")
        return super().__new__(cls)
    
    def __init__(self):
        print("Init called...")
        print("Object initalized...")

    def __del__(self):
        print("Destructor called...")
    
    def wish(self):
        print("Gm...")
obj1 = Test()
obj2 = obj1

del obj1  # __del__ not invoked... :-- Refrence counting

obj2.wish()