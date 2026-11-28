import requests
'''
  API :- GET,POST,PUT,DELETE,PATCH
  requests.get()
'''
import json
try:
    response = requests.get("https://dummyjson.com/products")
    data = response.json() # dict/list
    with open("product.json","w") as f:
        json.dump(data,f,indent=5)
        print("Operation success....")
except Exception as e:
    print(e)    