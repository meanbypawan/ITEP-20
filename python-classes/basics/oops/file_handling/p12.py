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
json_string = json.dumps(p)
print(json_string)