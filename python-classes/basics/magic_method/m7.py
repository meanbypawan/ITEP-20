# can we access static variable inside init method
# Ans:- we can call static varaible inside init method using class name 
# and by using self
# can we call static varible inside the instance method
# Ans : yes
# can we call static variable inside the class method
# Ans : yes
# can we call static/class variable inside the static method
class Test:
    a = 100 # static
    def __init__(self):
        self.b = 200
        #print(f"Inside init a : {Test.a}")
        print(f"Inside init a : {self.a}")
    def m1(self):
        #print(f"Inside m1 : {Test.a}")
        print(f"Inside m1 : {self.a}")
    
    @classmethod
    def m2(cls):
        print(f"Inside m2 {Test.a}")
        print(f"Inside m2 : {cls.a}")
    
    @staticmethod
    def say_hello():
        print(f"Hello Friends...")

obj = Test()
print(Test.__dict__)