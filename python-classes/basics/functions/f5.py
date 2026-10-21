# a and b :- positional argument
# *c :- it is variable length positional argument
def f1(a,b,*c):
    print(f"a : {a}")
    print(f"b : {b}")
    print(f"c : {c}")

f1(10,20,40,50,60)    

