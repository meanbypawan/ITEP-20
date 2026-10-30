class Operation:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def add(self):
        print(f"Addition : {self.__a + self.__b}")
    def multiplication(self):
        print(f"Multiplication : {self.__a * self.__b}")

obj1 = Operation(20,10)

obj1.add()
obj1.multiplication()