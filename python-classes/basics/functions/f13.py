x = 100
def f1():
    x = 200
    print(f"Inside f1  x : {x}") # 200
def f2():
    print(f"Inside f2 x : {x}") # 100

f1()
f2()

print(f"Outside x : {x}") # 100
