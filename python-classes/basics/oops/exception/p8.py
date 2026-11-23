'''
  exception (ZeroDivisionError,ValueError) as e:
'''
print("At the start..")

try:
  a = int(input("Enter 1st value.."))
  b = int(input("Enter 2nd value..")) # ValueError
  c = a / b   # ZeroDivisionError
  print(f"Result : {c}")

#except ZeroDivisionError:
#except (ZeroDivisionError):
#except (ZeroDivisionError) as e:
except ZeroDivisionError as e:  
  print("ZeroDivisionError Caught...")
  
print("At the end...")