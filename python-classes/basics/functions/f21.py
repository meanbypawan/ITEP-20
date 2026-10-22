
def f1():
    x = 100 # local to the f1
    print(f"Inside f1 x : {x}")

    def f2():
        x = 200  # Fresh assignment, it create new x which will be local to f2
        print(f"Insided f2 x : {x}")

    f2()
    print(f"Inside f2 at the end x : {x}")

    
f1()