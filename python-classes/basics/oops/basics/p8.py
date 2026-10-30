# Name Mangling
class Operation:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def set_a(self,a):
        self.__a = a    

    def set_b(self,b):
        self.__b = b    

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

obj1 = Operation(20,10)
print(f"a : {obj1.get_a()} b : {obj1.get_b()}")        

obj1.set_b(5)
print(f"a : {obj1.get_a()} b : {obj1.get_b()}")        
print(obj1.__dict__)
obj1._Operation__a = 500000
print(obj1._Operation__a)