class Message:
    
    def m1(self): # self :-  Refere current object
        print("m1-called...")

    def m2(self):
        print("m2-called...")
    
    def m3(self):
        print("m3-called...")        

    
obj = Message()
obj.m1() 
obj.m2()
obj.m3()        