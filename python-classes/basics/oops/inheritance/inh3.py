class A:
    def m1(self):
      print("A-m1")
      
    def m2(self):
       print("A-m2")

class B(A):
   def m1(self):
      print("B-m1..")

obj = B()
obj.m1()
obj.m2()         