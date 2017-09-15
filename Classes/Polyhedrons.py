class Cuboid:
    def __init__(self,s1,s2,s3):
        self.height = s1
        self.width = s2
        self.depth = s3
    def volume():
        return self.height * self.depth * self.width
    def surfaceArea():
        return self.height * self.length * 2 + self.height * self.depth * 2 + self.length * self.depth * 2
    def oppositeCornerDist():
        return math.sqrt(self.height**2 + self.length**2 + self.depth**2)

class Sphere:
    def __init__(self,radius):
        self.radius = radius
    def surfaceArea():
        return 4 * math.pi * (radius**2)
    def volume():
        return (4 * math.pi * (radius**3))/3
