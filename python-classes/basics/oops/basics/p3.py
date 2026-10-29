class Message:

    def m1(self):
        print("Instance method...")

    @classmethod
    def m2(cls):
        print("class method...")

    @staticmethod
    def m3():
        print("static method...")

    def m4():
        print("m4-called...")

obj = Message()
obj.m1()  # By using object

Message.m2() # By using classname

Message.m3() # By using classname

Message.m4()    