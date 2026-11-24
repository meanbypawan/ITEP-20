print("At the start...")
f = None
try:
  f = open("p1.py")
except FileNotFoundError as e:
  print("File not found..")
else:
  data = f.read()
  print(data)
finally:
  if f is not None:
    f.close()

print("At the end...")