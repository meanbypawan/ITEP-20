
# product : id,titl,price without using init method
class B:
    pass

class A(B):
    pass

class Product(A):
    def __new__(cls,id,title,price):
        obj = super().__new__(cls)
        obj.id = id
        obj.title = title
        obj.price = price
        return obj

    def __str__(self):
        return f"{self.id}:{self.title}:{self.price}"
    
p = Product(100,"Laptop",50000)    
print(p)
print(Product.mro())
print("object mro")
print(object.mro())
print(object.__dict__)