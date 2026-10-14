s = ",,,1A man, a plan,#### a canal: Panama1..."
s = s.lower()
print(s)
left = 0
right = len(s) - 1
while left < right:
    while left < right and (not s[left].isalnum()):
        left += 1
    while left < right and (not s[right].isalnum()):
        right -= 1
    if s[left] != s[right]:
        print("String is not palindrome")
        break
    left += 1
    right -= 1
else:
    print("String is palindrome")            
