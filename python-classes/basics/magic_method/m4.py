class Employee:
    def __init__(self,name,salary):
        self.salary = salary
        self.name = name
    def __add__(self,bonous):
        self.salary = self.salary + bonous
        return self
    def __str__(self):
        return f"Name : {self.name}, Salary : {self.salary}"
    
e1 = Employee("Cheeku", 90000)
e1 = e1 + 50000 # e1.__add__(50000)     
print(e1)