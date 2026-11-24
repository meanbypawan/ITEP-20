try:
    print("Outer Try Block")
    try:
      a = int(input("Enter 1st value..."))
      b = int(input("Enter 2nd value..."))
      c = a / b
    except ValueError as e:
       print("Value Error Caught...| Inner Except")
    finally:
       print("Inner Finally Block")

except ZeroDivisionError as e:
   print("ZeroDivisionError Caught..| Outer Except..")

finally:
   print("Outer Finally Block")               