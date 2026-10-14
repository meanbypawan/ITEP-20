# Replace every space with a hyphen (-).
s = "InfoBeans-Foundation"
# print(s)
# s = s.replace("-"," ")
# print(s)
s = list(s)
print(s)
for i in range(len(s)):
    if s[i] == "-":
        s[i] = " "
s = "".join(s)        
print(s)