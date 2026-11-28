import json
p = {
    "name":"ABC",
    "gender":"M",
    "fav_colo":("red","green","blue"),
    "contact_list":[1000,2000],
    "child":None,
    "married": True,
    "age":30,
    "height":5.7,
    "test": {1000:"OT",2000:"TT",4000:"FT"}
}

try:
    with open("test.json","a") as f:
        json.dump(p,f) # dumps() + write()
        print("Operation success..")
except OSError as e:
    print(e)