class Employee:
    
    def __new__(cls,id,name,salary):
       obj = super().__new__(cls)
       obj.id = id
       obj.name = name
       obj.salary = salary
       return obj
    
    def __str__(self):
        return f"{self.id}:{self.name}:{self.salary}"    

e1 = Employee(100,"A",120000) # __new__ --> __init__

print(e1)    # __str__