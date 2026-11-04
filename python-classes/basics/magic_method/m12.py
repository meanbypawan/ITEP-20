class Employee:
    def __new__(cls,id,name,salary):
        print("__new__ called...")
        return super().__new__(cls)
    
    def __init__(self,id,name,salary):
        print("__init__ called..")
        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.id}:{self.name}:{self.salary}"    

e1 = Employee(100,"A",120000) # __new__ --> __init__

print(e1)    # __str__