class Distance:
    def __init__(self,km,meter):
        self.km = km
        self.meter = meter
    def __add__(self,sd):
        temp = Distance(0,0)
        temp.km = self.km + sd.km
        temp.meter = self.meter + sd.meter
        if temp.meter >=1000:
            temp.km += 1
            temp.meter -= 1000
        return temp    
    def __str__(self):
        return str(self.km) +" km "+str(self.meter)+" meter"
     
d1 = Distance(7,300) 
d2 = Distance(2,900)
d3 = Distance(1,500)

d4 = d1 + d2 + d3 

print(f"First Distance  : {d1}")
print(f"Second Distance : {d2}")
print(f"Third Distance : {d3}") # d3.__str__
print(f"Result : {d4}")