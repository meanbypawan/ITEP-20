s = "a4b3cd2eee2"
# op = "aaaabbbcdcd"
word = ""
result = ""
for ch in s: # ch = "3"
   if ch.isdigit():
      result += word * int(ch)
      word = ""d
   else:
      word += ch  # word = "cd"
print(result)      