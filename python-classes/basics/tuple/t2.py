t1 = (1,2,3)
print(f"Before : {id(t1)}")
t1 = t1 * 3
print(f"After : {id(t1)}")
print(t1)

t2 = (10,20,30,40,50)
print(t2[1:4])