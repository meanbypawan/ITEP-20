class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    def __hash__(self):
        print("__hash__ called...")
        return hash(self.id)
    def __eq__(self, other):
        print("__eq__called...")
        return self.id == other.id
    def __str__(self):
        return f"{self.id} : {self.name} : {self.salary}"    

e1 = Employee(100,"A",90000)
e2 = Employee(101,"B",100000)
e3 = Employee(102,"C",150000)
e4 = Employee(100,"A",90000)
s = set()
s.add(e1)
s.add(e2)
s.add(e3)
s.add(e4)
for emp in s:
    print(emp)