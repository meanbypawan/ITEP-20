l = ["any","ant","etc","like","three","four"]

result = {}
for element in l:
    key = len(element)
    if key in result:
        result[key].append(element)
    else:
        result[key] = [element]
print(result)            

'''
    #o/p {3: ["any","ant","etc"], 4: ["like"], 5: ["three"]}
    result = {}

    result = {len(element):[] for element in l}
    #{3: [], 4: [], 5: []}

    for element in l:
        result[len(element)].append(element)

    print(result)    
'''

