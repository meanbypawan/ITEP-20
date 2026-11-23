class InsufficientBalanceError(Exception):
  pass

class InvalidVoterError(Exception):
  pass


age = int(input("Enter age : "))
try:
    if age < 18:
     raise InvalidVoterError()  
    else:
      print("Thank you for voting...")
except InvalidVoterError as e:
   print("Age must be greater or equals to 18")

finally:
  print("Thank you")   