def f1(a,b,/,c=10,*arg,d,**e):
    print(f"Positional a,b : {a},{b}")
    print(f"Default c : {c}")
    print(f"Var-arg arg : {arg}")
    print(f"Keyword only d : {d}")
    print(f"Var-key-arg e : {e}")

#f1(10,20,d=30)
f1(10,20,30,40,50,60,d=70,name="Atul",age=30)