# 1	2	2	4	8	32	…… n terms
n = int(input("Enter n : "))
if n >=2:
    a = 1
    b = 2
    print(a,end=" ")
    print(b,end=" ")
    for _ in range(n-2):
        c = a * b
        print(c,end=" ")
        a = b
        b = c
else:
    print("Input must be equal or greater then 2")        