# WAP to print table of a number
'''
  n  = 5
  5 X 1 = 5
  5 X 2 = 10
  5 X 3 = 15
  ...
  ...
  ...
  5 X 10 = 50
'''
n = int(input("Enter a number : "))
i = 1
while i <= 10:
    print(f"{n} X {i} = {n*i}")
    i += 1



