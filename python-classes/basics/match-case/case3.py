#n = 1
# 1 == True
#n = 1.5
#n = True
#n = "Indore"
#n = 20 + 5j
#n = [1,2,3]
#n = []
#n = (1,2)
#n = ()
#n = {"name":"Cheeku","age":21}
n = None
match n:
    case None: print("None matched...")
    case {"name":"Cheeku","age":21}: print("Dictionary Matched..")
    case (): print("Empty tuple matched...")
    case (1,2): print("Tuple matched...")
    case []: print("Empty list matched..")
    case [1,2,3]:print("List matched...")
    case 20+5j: print("Complex matched...")
    case "Indore": print("String matched...")
    case True: print("Boolean matched...")
    case 1: print("Integer matched...")
    case 1.5: print("Float matched....")
    case _: print("Not matched...")