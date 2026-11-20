print("At the start..")

try:
  a = int(input("Enter 1st value.."))
  b = int(input("Enter 2nd value..")) # ValueError
  c = a / b   # ZeroDivisionError
  print(f"Result : {c}")

except ValueError as e:
  print("Only integers are allowed..")

except ZeroDivisionError as e:
  #Exception Handling Code....
  print("Denominator can't be zero...")
  
print("At the end...")