from abc import ABC,abstractmethod

class Test(ABC):
    @abstractmethod
    def wish(self):
        pass
    
class TestIMPL(Test):
    def wish(self):
        print("GM....")

obj = TestIMPL()
obj.wish()