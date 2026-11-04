
class Test(object):
    def __new__(cls):
        print("__new__ called...")
        return super().__new__(cls)
           
    def __init__(self):
        print("init called...")

    def wish(self):
        print("Gm.....")

obj = Test() #         
obj.wish()
# print(obj)
# print(type(obj))