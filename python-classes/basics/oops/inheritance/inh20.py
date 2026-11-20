class Test:
    def f1(self):
        print("First")

    def f1(self,msg):
        print(f"Second : {msg}")


obj = Test()
obj.f1()