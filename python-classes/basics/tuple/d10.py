l = [1,2,3,4,5,6,10,15]

# o/p {1: "Odd", 2: "Even", "3": "Odd"...}

result = {element: "Odd" if element % 2  else "Even" for element in l}

print(result)