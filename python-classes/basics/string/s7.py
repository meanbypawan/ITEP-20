s = "aabbcabddefe"
result = {}
for ch in s:
   result[ch] =  result.get(ch,0)+1 # ch = "a"
print(result)   