from abc import ABC,abstractmethod
# Developer Level
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

# Programmer Level
class Circle(Shape):
    def get_area(self):
        radius = float(input("Enter radius.."))
        print(f"Circle Area : {3.14 * radius * radius}")    

# Programmer Level
class Rectangle(Shape):
    def get_area(self):
        length = float(input("Enter length.."))
        width = float(input("Enter width..."))
        print(f"Rectangle Area : {length * width}")

#Programmer Level
class Traingle(Shape):
    def get_area(self):
        base = float(input("Enter base..."))
        height = float(input("Enter height.."))
        print(f"Traingle Area : {0.5 * base * height}")

s = None
print("1 for circle")
print("2 for rectangle")
print("3 for traingle")
choice = int(input("Enter your choice : "))
if choice == 1:
    s = Circle()
elif choice == 2:
    s = Rectangle()
elif choice == 3:
    s = Traingle()

s.get_area()