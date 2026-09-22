n = int(input("Enter a value b/w 1 to 5 : "))
a = 2
b = 1
match n:
    case 1: print("One")
    case 2: print("Two")
    case 3: print("Three")
    case 4: print("Four")
    case 5: print("Five")
    case _: print("Invalid value...")