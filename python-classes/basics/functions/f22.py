
def f1():
    x = 100 
    print(f"Inside f1 x : {x}")

    def f2():
        nonlocal x
        x = x + 10  
        print(f"Insided f2 x : {x1}")

    f2()
    print(f"Inside f2 at the end x : {x}")

    
f1()