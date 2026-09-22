'''
 per > 90 : Grade A
 per >=80 and per <=90  Grade B
 per >=60 and per <80 Grade C
 Otherwise D
'''
per = float(input("Enter student percentage : "))
match per:
   case per if per > 90: print("A Grade")
   case per if per >=80 and per < 90 : print("B Grade")
   case per if per>=60 and per < 80: print("C Grade")
   case _:print("D Grade")





