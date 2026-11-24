
try:
    with open("abc.txt","r") as f:
        data = f.read()
        print(data)

except OSError as e:
    print(e)
    
print(f.closed)    