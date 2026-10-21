x = 100

def f1():
    a = 500
    print(f"Inside f1 x : {x}") # global
    print(f"Inside f1 a : {a}") # local

f1()
print(f"Outside x : {x}")
print(f"Outside a : {a}")