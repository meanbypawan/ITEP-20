'''
  dictionary object / list ------> JSON

  dump()
  dumps()

  load()
  loads()
'''
import json
p = {
    "id":100,
    "name":"Mouse",
    "price": 500,
    
}
json_string = json.dumps(p)
print(type(json_string))
print(json_string)

# json_string --> Python dict object
po = json.loads(json_string)
print("*"*10)
print(type(po))
print(po)