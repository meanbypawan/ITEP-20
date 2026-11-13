class A:
    def wish(self):
        print("GM..")

class B:
    def wish(self):
        print("GE..")

class C(B,A):
    pass

obj = C()
obj.wish()