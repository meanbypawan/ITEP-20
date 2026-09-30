arr = [1,4,3,6,9,8,11]

even_list = [i for i in arr if i%2==0]
odd_list = [i for i in arr if i%2]

result = odd_list + even_list
print(f"Odd : {odd_list}")
print(f"Even : {even_list}")
print(f"Result : {result}")
