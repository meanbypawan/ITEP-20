from abc import ABC,abstractmethod
class Test(ABC):
    @abstractmethod
    def __init__(self):
        pass

class TestImpl(Test):
    def __init__(self):
        print("Executed...")

obj = TestImpl()
print(obj)
    