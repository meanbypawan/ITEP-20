print("At the start..")

a = int(input("Enter 1st value.."))
b = int(input("Enter 2nd value.."))
try:
  c = a / b
  print(f"Result : {c}")
except ZeroDivisionError as e:
  print(e)
  
print("At the end...")