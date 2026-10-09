product = {
    "id":1000,
    "title":"Laptop",
    "price":50000
}

product["discounterPercentage"] = 10.2

for key in product.keys():
    print(f"{key} : {product[key]}")

print("*"*20)

for value in product.values():
    print(f"Value : {value}")

print("*"*50)

for key,value in product.items():
    print(f"{key} : {value}")