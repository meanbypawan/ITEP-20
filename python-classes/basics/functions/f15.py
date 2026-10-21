x = 100
def f1():
    global x
    x = 200
    print(f"Inside f1 x  {x}") # 200

f1()
print(f"Outside x : {x}") # 100   