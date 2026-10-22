def f1():
    print("f1-called...")
    def f2():
        print("f2-called...")
    return f2


inner = f1()
inner()