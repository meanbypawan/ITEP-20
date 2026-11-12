'''
  Area : (l,w)
         get_area()
  Volume :(l,w,h)
         : get_area()
         : get_volume()   
'''

class Area:
    def __init__(self,l,w):
        self.__l = l
        self.__w = w

    def get_area(self):
        return self.__l * self.__w 
       
    def get_l(self):
        return self.__l
    
    def get_w(self):
        return self.__w

class Volume(Area):
    def __init__(self,l,w,h):
        super().__init__(l,w)
        self.__h = h
    def get_volume(self):
        #return self.__l * self.__w * self.__h
        return self.get_l() * self.get_w() * self.__h
    
v = Volume(2,3,4)
print(f"Area : {v.get_area()}")
print(f"Volume : {v.get_volume()}")
#print(v.__dict__)
# obj = Area(2,3)
# print(f"Area : {obj.get_area()}")    