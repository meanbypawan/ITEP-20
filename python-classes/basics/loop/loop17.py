#arr = [1,2,3,7,5]
arr = [1,2,3,4,5,6,7,8,9,10]
target = 15
cs = 0
left = 0
for right in range(len(arr)):
   cs += arr[right]
   while cs > target and left <= right:
      cs -= arr[left]
      left += 1
   if cs == target:
      print(f"[{left+1},{right+1}]")
      break
else:
   print(f"No subarray exist..")      