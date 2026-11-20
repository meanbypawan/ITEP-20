from abc import ABC,abstractmethod
class __Area(ABC):
    def __init__(self,l,w):
        self.__l = l
        self.__w = w

    @abstractmethod
    def get_area(self):
        pass    
    def get_l(self):
        return self.__l
    def get_w(self):
        return self.__w

class AreaImpl(__Area):
    def __init__(self,l,w):
        super().__init__(l,w)

    def get_area(self):
        return self.get_l() * self.get_w()

obj = AreaImpl(2,3)

print(f"Area : {obj.get_area()}")
