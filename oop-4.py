#property 
from math import pi
class circle:
    def __init__(self,radius):
        self.radius = radius
    
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,radius):
        self.__radius = radius
        
    @property
    def area(self):
        return self.radius**2 * pi
    
    @property
    def parame(self):
        return 2 * self.radius * pi

c1 = circle(5)

print(c1.area)
print(c1.parame)
