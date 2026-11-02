class Customer:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.balance = balance
    
    def __str__(self):
        print("__str__ called...")
        return str(self.id)+":"+self.name+":"+str(self.balance)
    
obj = Customer(100,"Atul",100000) # obj {id:100, name: "Atul",balance : 100000}
print(obj)