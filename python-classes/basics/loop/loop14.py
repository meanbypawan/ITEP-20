arr1 = [2,3,3,4,5]
arr2 = [1,3,4,4,6,7,8]
result = []
i = 0
j = 0
while (i < len(arr1)) and (j < len(arr2)):
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j+= 1

while i < len(arr1):
    result.append(arr1[i])
    i+=1            

while j < len(arr2):
    result.append(arr2[j])
    j += 1

print(f"arr1 : {arr1}")
print(f"arr2 : {arr2}")
print(f"result : {result}")