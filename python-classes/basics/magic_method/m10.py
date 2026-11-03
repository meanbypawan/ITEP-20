class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
    
    def __str__(self):
        return f"{self.id} : {self.name} : {self.salary}"    

e1 = Employee(100,"AA",95000)
e2 = Employee(101,"B",100000)
e3 = Employee(102,"C",150000)
e4 = Employee(100,"AA",90000)
s = set()
s.add(e1)
s.add(e2)
s.add(e3)
s.add(e4)
for emp in s:
    print(emp)