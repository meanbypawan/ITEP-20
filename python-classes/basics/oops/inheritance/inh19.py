class A:
    def m1(self,msg):
        print(f"Parent A :{msg}")

class B(A):
    def m1(self):
        print("B-m1..")

obj = B()
obj.m1()                