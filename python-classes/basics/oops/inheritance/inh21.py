class Outer:
    class Inner:
        def m1(self):
            print("Inner m1...")

#obj = Outer()
inner = Outer().Inner()
inner.m1()            