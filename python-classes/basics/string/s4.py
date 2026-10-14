#Count uppercase letters, lowercase letters, digits, and special characters
# isupper()
# islower()
# isdigit()
# A :- 65
# a :- 97
# 48 

s = "InDOrE#143"
uc = lc = dc = sc = 0
for ch in s:
   ascii = ord(ch)
   if  ascii >= 65 and ascii <= 90:
      uc += 1
   elif ascii >=97 and ascii <=122:
      lc += 1
   elif ascii >=48 and ascii <=57:
      dc += 1
   else:
      sc += 1
print(f"Upper count :{uc}")
print(f"Lower count : {lc}")
print(f"Digit count : {dc}")
print(f"Special count : {sc}")                
