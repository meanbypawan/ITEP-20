l = [1,2,3,4,5]
# o/p {1:1,2:4,3:9,4:16,5:25}

result = {element: element*element for element in l}

# result = {}
# for element in l:
#     result[element] = element**2

print(result)    

#String :-