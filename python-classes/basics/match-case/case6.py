while True:
    print("Press 1 for addition : ")
    print("Press 2 for subtraction : ")
    print("Press 3 for multiplication : ")
    print("Press E/e for exit : ")
    choice = input("Enter your choice : ")
    match choice :
        case "1": 
                a = float(input("Enter 1st value : "))
                b = float(input("Enter 2nd value : "))
                print(f"Addition : {a+b}")
        case "2":
                a = float(input("Enter 1st value : "))
                b = float(input("Enter 2nd value : "))
                print(f"Sub : {a-b}")            
        case "3":
                a = float(input("Enter 1st value : "))
                b = float(input("Enter 2nd value : "))
                print(f"Mulitplication : {a*b}")
        case "E"|"e": break
        case _: print("Invalid choice...")
                                  