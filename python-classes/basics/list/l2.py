import sys
l1 = [10,20,30]

print(f"Data : {l1}")
print(f"len : {len(l1)}")
print(f"Size : {sys.getsizeof(l1)}") #
# Adding element into the list

l1.append(100)

print("After append 100")
print(f"Data : {l1}")
print(f"len : {len(l1)}")
print(f"Size : {sys.getsizeof(l1)}") #

l1.append(200)
print("After appending 200")
print(f"Data : {l1}")
print(f"len : {len(l1)}")
print(f"Size : {sys.getsizeof(l1)}") #
