# customer 
# property :- id,name,contact,account_no
# behavour :- view_details()

# constructor
'''
  class Customer{
     int id
     String name
     String contact
     String account_no
  }
'''

class Customer:
    def __init__(self,id,name,contact,account_no):
        self.id = id
        self.name = name
        self.contact = contact
        self.account_no = account_no

    def view_details(self):
      print(f"Id : {self.id}\nName :{self.name}\nContact:  {self.contact}\nAccount : {self.account_no}")

obj1 = Customer(100,"Atul",9009111222,"ac1001")# {"id":100,"name":'Atul',.....}
obj2 = Customer(101,"Ankita",9009111333,"ac1002")# {"id":101,"name":"Ankita",....}
obj3 = Customer(102,"Rahil",9009111444,"ac1003") # {"id":"102","name":"Rahil",...}

obj3.view_details()