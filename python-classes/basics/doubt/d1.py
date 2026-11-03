# Closure : Functions bundled together
# Decorator
#-------------------

def f1():
    x = 100
    print(f"Insided f1 : {x}")
    def f2():
        print(f"Inside f2 : {x}")
    return f2

f2 = f1()    
# 1000 line code
f2()