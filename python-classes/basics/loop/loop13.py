l1 = [10,20,30,40,50]
item = int(input("Enter an element : "))
for i in range(len(l1)):
    if item == l1[i]:
        print(f"Element found at index : {i}")
        break
else:
    print("Element Not Found")    