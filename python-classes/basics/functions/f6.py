# positional only argument
def f1(a,b,c,/):
    print(f"a : {a}")
    print(f"b : {b}")
    print(f"c : {c}")

f1(10,20,c = 30)    