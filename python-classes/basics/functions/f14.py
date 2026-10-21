x = 100
def f1():
    global x
    x = x + 10
    print(f"Inside f1  x : {x}") # 110

f1()
print(f"Outside x : {x}") # 110
