class Product:
    def __init__(self,id,title,price,brand,description):
        self.__id = id
        self.__title = title
        self.__price = price
        self.__brand = brand
        self.__description = description
        
    def __getstate__(self):
        print("Get State called...")
        return {
            "product_id":  self.__id,
            "product_title": self.__title,
            "product_price":self.__price,
            "product_brand": self.__brand
        }
    def __setstate__(self,state):
        print("setstate called.......")
        print(state)
        self.__id = state["product_id"]
        self.__title = state["product_title"]
        self.__price = state["product_price"]
        self.__brand = state["product_brand"]
        

    def __str__(self):
        return f"{self.__id}:{self.__title}:{self.__price}:{self.__brand}"    