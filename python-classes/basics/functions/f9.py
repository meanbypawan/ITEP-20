def f1(a,*b,**c):
    print(f"Positional : {a}")
    print(f"Var-arg : {b}")
    print(f"Var-key-arg : {c}")

f1(10,20,30,40,name="Atul",age=40)    