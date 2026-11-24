f = None
try:
    f = open("python_intro.txt","x")
    data = input("Enter some text : ")
    f.write(data)
except OSError as e:
    print(e)
finally:
    if f is not None:
        f.close()    
print("At the end...")        