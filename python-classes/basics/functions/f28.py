def f1(callback):
    print("F1-called..")
    print(callback)
    callback()
    
def f2():
    print("F2-called...")

a = f2
f1(a)    
