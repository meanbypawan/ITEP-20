'''
  -6 -3 0 3 6
  -9 -6 -3 0 3 6 9
'''
n = int(input("Enter value of n : "))
if n%3 == 0:
  for i in range(-n,n+1,3):
    print(i,end="  ")
  print()  