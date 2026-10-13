l = ["apple","ant","bat","banana","cat","cherry"]
result = {}

for str in l:
    key  = str[0]
    if key in result:
        result[key].append(str)
    else:
        result[key] = [str]
print(result)            