def decorator(func):
  print("Before....")
  func()
  print("After.....")

def say_hello():
    print("Hello...")

decorator(say_hello)

#say_hello()