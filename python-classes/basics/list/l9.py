x = [[1,2,3],
     [4,5,6,7,9],
     [7,8]]
# len(x[0]) ==> 3
# len(x[1]) ==> 5
# len(x[2]) ==> 2
# index based
for r in range(len(x)):
    for c in range(len(x[r])):
        print(x[r][c],end=" ")
    print()    