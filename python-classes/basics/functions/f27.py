y = 100
def f1():
    x = 200
    def f2():
        global y
        print(f"y : {y}")
        nonlocal x
        print(f"x : {x}")
    f2()
f1()        
        