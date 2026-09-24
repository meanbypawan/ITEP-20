x = [10,20,30,40,50]
print(f"List Element : {x}")
print(f"Type of list : {type(x)}")
print(f"Length of the list : {len(x)}")

# index based access
for i in range(len(x)):
    print(f"Index : {i} Value : {x[i]}")

# Element wise access
for element in x:
    print(f"{element}")
