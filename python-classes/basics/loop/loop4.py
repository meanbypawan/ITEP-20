n = int(input("Enter a number : "))
i = 2
status = False
while i <= (n//2):
    if n % i == 0:
        status = True
        break
    i += 1

if status or n < 2:
    print("Not prime")
else:
    print("Prime")    