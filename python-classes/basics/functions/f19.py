def outer():
    x = 100
    print(f"Insided outer x : {x}")
    def inner():
        print(f"Inside inner x : {x}")

    return inner    

i = outer()
#10000 line of code
i()    