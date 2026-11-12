#super()
class A:
    @classmethod
    def m1(cls):
      print("A-m1")
      print(type(cls()))
      
    def m2(self):
       print("A-m2")

class B(A):

   @classmethod
   def m1(cls):
      super().m1() # super(B,B).m1()
      print("B-m1..")
 
obj = B()
B.m1()         