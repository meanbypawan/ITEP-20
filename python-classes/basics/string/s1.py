s1 = "indore"
l = list(s1)
left = 0
right = len(l)-1
while left < right:
    l[left],l[right] = l[right],l[left]
    left += 1
    right -= 1

result = "".join(l)    
print(result)