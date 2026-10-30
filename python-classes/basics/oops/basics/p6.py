class Operation:
    def __init__(self,a,b):
        print("Init called....")
        self.a = a
        self.b = b
    def add(self):
        print(f"Addition : {self.a+self.b}")

obj1 = Operation(20,10)
obj1.add()
print(obj1.__dict__)
print(f"Multiplication : {obj1.a * obj1.b}")