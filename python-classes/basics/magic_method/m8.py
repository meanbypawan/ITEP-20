class Test:
    __counter = 0
    def __init__(self):
       Test.__counter += 1

    @classmethod
    def get_count(cls):
        return cls.__counter
    
t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()
print(f"Total Object : {Test.get_count()}")