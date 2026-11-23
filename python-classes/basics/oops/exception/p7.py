print("At the start..")

try:
  a = int(input("Enter 1st value.."))
  b = int(input("Enter 2nd value..")) # ValueError
  c = a / b   # ZeroDivisionError
  print(f"Result : {c}")

except (ValueError,ZeroDivisionError) as e:
  print("Oops! something went wrong...")
  print(e.__class__.__name__)
  
print("At the end...")