def f1():
    x = 100
    def f2():
        def f3():
           nonlocal x
           x = x + 1
           print(f"Inside f3 x : {x}")
        
        f3()
    f2()

f1()