'''
 1 4 9 16 25 ... n-terms

 '''
n = int(input("Enter n : "))
i = 1
while n!=0:
    print(i*i, end=" ")
    n = n - 1
    i = i + 1

print()