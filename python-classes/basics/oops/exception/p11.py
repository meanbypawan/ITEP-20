print("At the start..")
try:
  a = int(input("Enter 1st value.."))
  b = int(input("Enter 2nd value..")) # ValueError
  c = a / b   # ZeroDivisionError
  print(f"Result : {c}")

except Exception as e:
  print(f"{e.__class__.__name__} Oops! something went wrong")

finally:
  print("Hello...")

print("At the end...")