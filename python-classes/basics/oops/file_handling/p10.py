import pickle
from product import Product
def write_product(p):
    try:
        with open("product.pkl","w+b") as f:
            pickle.dump(p,f)
            print("Operation Success....")
    except OSError as e:
        print(e)

def read_product():
    try:
        with open("product.pkl","rb") as f:
            while True:
                p = pickle.load(f)
                print(p)
    except EOFError as e:
        print("EOF..")
    except OSError as e:
        print(e)                        

# p = Product(100,"Laptop",100000,"Dell","Core i11")
# write_product(p)
read_product()