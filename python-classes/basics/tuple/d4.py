product_list = [
    {"id":100,"title":"p1","price":50000},
    {"id":101,"title":"p2","price":60000},
    {"id":102,"title":"p3","price":40000}
]

for p in product_list:
    print(f"{p["id"]}\t{p["title"]}\t{p["price"]}")