t = (10,20,30,40,40,50,60,60)

for i in range(len(t)):
    print(f"{i} {t[i]}")

t1 = (1,2,3)  #139087289932224

t2 = (4,5,6)

print(f"Before : {id(t1)} ")
t1 = t1 + t2 # 139087291020768
print(f"After : {id(t1)}")
print(t1)
