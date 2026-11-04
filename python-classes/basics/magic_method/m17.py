import gc

class Test:
    def __init__(self):
        print("init called...")

    def __del__(self):
        print("del called...")    

gc.disable()
print(f"isEnabled : {gc.isenabled()}")

obj = Test()
del obj