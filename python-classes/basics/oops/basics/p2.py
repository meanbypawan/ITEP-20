class Message:
    
    def m1(self): # self :-  Refere current object
        print("Instance method")

    @classmethod
    def m2(cls):
        print("Class method...")
    
obj = Message()
obj.m1()
Message.m2()