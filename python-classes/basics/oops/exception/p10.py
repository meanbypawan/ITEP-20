'''
  exception (ZeroDivisionError,ValueError) as e:
'''
print("At the start..")

try:
  a = int(input("Enter 1st value.."))
  b = int(input("Enter 2nd value..")) # ValueError
  c = a / b   # ZeroDivisionError
  print(f"Result : {c}")

except:
  print(f"Oops! something went wrong...")  


print("At the end...")