arr = [1,5,6,8,7,9]
target = 12
result = []
flag = False
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if (arr[i]+arr[j]) == target:
            result.extend([i,j])
            print(result)
            break
    if result:
        break    