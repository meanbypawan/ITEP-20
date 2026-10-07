A = [[2,2,2],[3,3,3],[4,4,4]]
B = [[2,2,2],[3,3,3],[4,4,4]]

C = [[0]*3,[0]*3,[0]*3]

print("A Matrix")
print("*"*10)
for ri in range(len(A)):
    for ci in range(len(A[ri])):
        print(A[ri][ci],end=" ")
    print()

print("B Matrix")
print("*"*10)
for ri in range(len(B)):
    for ci in range(len(B[ri])):
        print(B[ri][ci],end=" ")
    print()

# print("C Matrix")
# print("*"*10)
# for ri in range(len(C)):
#     for ci in range(len(C[ri])):
#         print(C[ri][ci],end=" ")
#     print()

# Addition Logic
print("Addition of A and B : ")
for ri in range(len(A)):
    for ci in range(len(A[ri])):
        C[ri][ci] = A[ri][ci] + B[ri][ci]
        print(C[ri][ci],end=" ")
    print()        