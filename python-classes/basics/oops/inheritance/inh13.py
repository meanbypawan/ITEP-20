from abc import ABC,abstractmethod

class Test(ABC):
    @abstractmethod
    def wish(self):
       print("GN......")
    
    def say_hello(self):
        print("Hello...")

class TestIMPL(Test):
    def wish(self,message):
        #super().wish()
        print(f"{message}")
    
obj = TestIMPL()
obj.wish("Hello...")