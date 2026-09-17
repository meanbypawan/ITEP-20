'''
 1	+	1/2	+	1/3	+	1/4	+	1/5	….. n
 1/1 + 1/2 ........................1/n
 '''
n = int(input("enter n : "))
sum = 0

for i in range(1,n+1):
    sum = sum + 1 / i
    
print(f"Total sum : {sum:.2f}")