import math

class Circle:
    def __init__(self, radius=1):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = radius
        self.__diameter = radius * 2
        self.__area = math.pi * radius ** 2

    @property
    def radius(self):
        return self.__radius

    @property
    def diameter(self):
        return self.__diameter

    @property
    def area(self):
        return self.__area

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = r
        self.__diameter = 2 * r
        self.__area = math.pi * r**2

    @diameter.setter
    def diameter(self,d):
        self.__diameter = d
        self.__radius = d / 2
        self.__area = math.pi * self.__radius ** 2

    @area.setter
    def area(self, a):
        raise AttributeError()

     

    def __repr__(self):
        return f"Circle({self.radius})"

    

