class Test:
    def _m1(self):
        print("m1-called...")

print(Test.__dict__)
obj = Test()
obj._m1()        