x = 200
def f1():
    x = 100
    print(f"Inside f1 : {x}")
def f2():
    global x
    x = x + 10
    print(f"Inside f2 : {x}")

f1()
f2()
print(f"Global x : {x}")