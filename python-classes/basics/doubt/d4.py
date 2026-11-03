def f1():
    x = 100
    def f2():
        nonlocal x
        x = x + 10
        print(f"Inside f2 : {x}")

    f2()


f1()