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
    def __init__(self):
        self.id = 100
        self.name = "Atul"
        self.contact = 9009111222
        self.account_no = "ac10001"

    def view_details(self):
      print(f"Id : {self.id}\nName :{self.name}\nContact:  {self.contact}\nAccount : {self.account_no}")

obj = Customer() # obj = {"id":100, "name": "Atul", "contact":9009111222,"account_no": "ac10001"}
obj.view_details()