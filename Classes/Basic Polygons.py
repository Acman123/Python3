class Polygon(object):
    def __init__(self,id1,sides,area):
        self.id = id1
        self.noSides = len(sides)
        self.area = area
        self.sides = sides
        if None not in sides:
            self.perimeter = sum(sides)
        
class Rectangle(Polygon):
    def __init__(self,id1,width,height):
        self.height = height
        self.width = width
        self.area = self.height * self.width
        super(self.__class__,self).__init__(id1,4)
        
class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.diameter = radius * 2
    def area(self):
        return math.pi * (self.radius**2)
    def circumference(self):
        return math.pi * self.diameter
    def arc(self, a):
        return self.circumference() * (a/360)
    
    def sector(self, a):
        return self.area() * (a/360)

class Square(Rectangle):
    def __init__(self,width,height):
        super(self.__class__,self).__init__(id1,4,width,height)
    def diagonal():
        return pythagoras('ss',self.width,self.length)
    def perimiter():
        return 2 * self.length + 2 * self.width
