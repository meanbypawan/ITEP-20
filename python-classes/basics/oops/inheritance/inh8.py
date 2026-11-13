class Area:
    def __init__(self,l,w):
        self.__l = l
        self.__w = w

    def get_area(self):
        return self.__l * self.__w    

class Volume(Area):
    def __init__(self,l,w,h):
        super().__init__(l,w)
        self.__h = h
    def get_volume(self):
        return self.get_area() * self.__h

class Density(Volume):
    def __init__(self,l,w,h,m):
        super().__init__(l,w,h)
        self.__m = m
    def get_density(self):
        return self.__m / self.get_volume()                

d = Density(1,2,3,4)
print(f"Area : {d.get_area()}")
print(f"Volume : {d.get_volume()}")
print(f"Density : {d.get_density():.2f}")    