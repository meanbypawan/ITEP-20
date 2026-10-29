x = [1,2,3,4,5,6,7,8,9,10]

result = tuple(filter(lambda n: n%3 == 0 or n%5 == 0,x))
print(result)