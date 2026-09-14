a = int(input("Enter 1st value : "))
b = int(input("Enter 2nd value : "))

print(f"Before swapping a : {a} and b : {b}")

a = a ^ b
b = a ^ b
a = a ^ b

print(f"After swapping a : {a} and b : {b}")