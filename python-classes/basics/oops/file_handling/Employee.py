class Employee:
    def __init__(self,id,name,contact,age,company):
        self.__id = id
        self.__name = name
        self.__contact = contact
        self.__age = age
        self.__company = company

    def __str__(self):
        return f"{self.__id}:{self.__name}:{self.__contact}:{self.__age}:{self.__company}"    
    