x = 100
def f1():
    x = 200
    def f2():
        def f3():
            #nonlocal x
            global x
            x = x + 10
            print(f"Insided f3 {x}")
        f3()
    f2()

f1()            