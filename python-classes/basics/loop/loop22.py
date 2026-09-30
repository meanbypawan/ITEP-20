arr = [1,2,3,4,5,6,8,10]
# o/p [odd,even,odd,even,odd,even,even,even]
result = ["Even" if x%2==0 else "Odd" for x in arr]
print(arr)
print(result)