d = {"a":100,"b":200,"c":300,"d":400,"e":500}
# o/p {100:"a",200:"b",300:"c",400:"d",500:"e"}

result = {value: key for key,value in d.items()}
print(result)