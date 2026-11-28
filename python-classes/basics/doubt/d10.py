class A:
    # def m1(self):
    #     print("A-m1")
    pass
class B:
    def m1(self):
        print("B-m1")

class C(A,B):
    pass

obj = C()
obj.m1() 
print(C.mro())               