import gc
class First:
    def __init__(self):
        print("First init called...")

    def __del__(self):
        print("First del called...")    

class Second:
    def __init__(self):
        print("Second init called..")
    def __del__(self):
        print("Second del called...") 

first = First()
second = Second()

first.link = second
second.link = first

del first
del second

# gc.collect()

print("Hello....")