# 1	2	2	4	8	32	…… n terms
n = int(input("Enter n : "))
a = 1
b = 2
for _ in range(n):
    print(a,end=" ")
    c = a * b
    a = b
    b = c
print()    
