x = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda n: not n%2,x))
print(f"Type : {type(result)}")
print(f"Result  {result}")