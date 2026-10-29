#map() ---> Transform
#filter()--> Filteration
x = [1,2,3,4,5]

# def square(n):
#     return n*n

result = list(map(lambda n: n*n,x))

print(f"Type of result : {type(result)}")
print(f"Result : {result}")