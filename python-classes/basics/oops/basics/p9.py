# Library Management :- Book, Student, Admin
# CMS :-- Faculty, Student, PayRol.....
# E-commerce :- Product, Category, User, Cart, Order
# Time---> hrs, min, sec
# t3.add(t1,t2)
class Distance:
    def __init__(self,km,meter):
        self.__km = km
        self.__meter = meter

    def add(self,sd):
        temp = Distance(0,0)
        temp.__km = self.__km + sd.__km
        temp.__meter = self.__meter + sd.__meter
        if temp.__meter >= 1000:
            temp.__km += 1
            temp.__meter -= 1000
        return temp
    
    def display(self):
        print(f"{self.__km} km {self.__meter} meter")        

d1 = Distance(7,600)
d2 = Distance(2,700)
d1.display()
d2.display()
d3 = d1.add(d2)
print("After add..")
d3.display()
