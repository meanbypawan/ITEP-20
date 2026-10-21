def f1(a,b,/,*,c,d):
    print(f"a : {a}")
    print(f"b : {b}")
    print(f"c : {c}")
    print(f"d : {d}")

f1(10,20,c = 30,d = 40)    