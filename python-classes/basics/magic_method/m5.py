class Product:
    def __init__(self,id,title,price):
        self.id = id
        self.title = title
        self.price = price
    
    def __eq__(self, sp):
        if self.id == sp.id and self.title == sp.title and self.price == sp.price:
            return True
        return False

p1 = Product(100,"Laptop",90000)
p2 = Product(100,"Laptop",99000)

print(p1 == p2) # p1.__eq__(p2)