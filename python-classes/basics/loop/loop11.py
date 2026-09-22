for i in range(1,6):
    for _ in range(5,i,-1):
        print(" ",end="")
    for j in range(i,1,-1):
        print(j,end="")
    for j in range(1,i+1):
        print(j,end="") 
    print()       