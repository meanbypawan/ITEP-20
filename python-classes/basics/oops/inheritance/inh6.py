#super()
class A:
    @staticmethod
    def m1():
      print("A-m1")
      
    def m2(self):
       print("A-m2")

class B(A):

   @staticmethod
   def m1():
      #super().m1() --> Error
      print("B-m1..")
 
B.m1()         