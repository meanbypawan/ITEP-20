first_value = int(input("Enter 1st value : "))
second_value = int(input("Enter 2nd value : "))
third_value = int(input("Enter 3rd value : "))

'''
max = first_value if first_value > second_value else second_value

print(f"{max} is greater") if max > third_value else print(f"{third_value} is greater")
'''
print(f"{first_value} is greater") if first_value > second_value and first_value > third_value else print(f"{second_value} is greater") if second_value > third_value else print(f"{third_value} is greater")