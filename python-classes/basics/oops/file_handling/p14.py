import json
try:
    with open("test.json","r") as f:
        data  = json.load(f)
        print(type(data))
        print(data)
except OSError as e:
    print(e)