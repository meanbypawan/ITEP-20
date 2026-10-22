def f1():
    print("F1-called...")
    def f2():
        print("F2-called...")
        def f3():
            print("F3-called...")
        return f3
    return f2

f2 = f1()
f3 = f2()
f3()    