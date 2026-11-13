from abc import ABC,abstractmethod
class Test(ABC):
   
   @classmethod
   @abstractmethod
   def wish(cls):
      print("GM...")

   @staticmethod
   @abstractmethod
   def say_hii():
      print("Hii...")

   def say_hello(self):
      print("Hello...") 

class TestIMPL(Test):
   def wish(self):
      print("GN......")
   @staticmethod
   def say_hii():
      print("Hiii How r u?")

obj = TestIMPL()
obj.wish()
obj.say_hello()
