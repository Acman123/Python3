import cmath
import math
import gc

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


class Triangle(Polygon):
    def __init__(self, id1, lengths, angles):
        self.sides = list(lengths)
        self.angles = list(angles)
        self.id = id1
        self.a = self.sides[0]
        self.b = self.sides[1]
        self.c = self.sides[2]
        self.A = self.angles[0]
        self.B = self.angles[1]
        self.C = self.angles[2]

        try:
            self.A
            if self.A == 0:
                raise AttributeError
        except AttributeError:
            self.A = None

        try:
            self.B
            if self.B == 0:
                raise AttributeError
        except AttributeError:
            self.B = None

        try:
            self.C
            if self.C == 0:
                raise AttributeError
        except AttributeError:
            self.C = None

        try:
            self.a
            if self.a == 0:
                raise AttributeError
        except AttributeError:
            self.a = None

        try:
            self.c
            if self.c == 0:
                raise AttributeError
        except AttributeError:
            self.c = None

        try:
            self.b
            if self.b == 0:
                raise AttributeError
        except AttributeError:
            self.b = None

        self.angles = [self.A, self.B, self.C]
        self.sides = [self.a,self.b,self.c]

        if self.a and self.b and self.c:
            if not self.A:
                self.A = cosineRule('A', self.a, self.b, self.c, self.A, self.B, self.C)[0][1]
            if not self.B:
                self.B = cosineRule('B', self.a, self.b, self.c, self.A, self.B, self.C)[0][1]
            if not self.C:
                self.C = cosineRule('C', self.a, self.b, self.c, self.A, self.B, self.C)[0][1]

        self.angles = [self.A, self.B, self.C]
        self.sides = [self.a,self.b,self.c]

        if len(self.angles) - self.angles.count(0) == 2:
            if (not self.A) and (None not in self.angles[1:]):
                self.A = 180 - (self.B + self.C)
            if not self.B and (None not in (self.A,self.C)):
                self.B = 180 - (self.A + self.C)
            if not self.C and (None not in self.angles[:-1]):
                self.C = 180 - (self.B + self.A)

        self.angles = [self.A, self.B, self.C]
        self.sides = [self.a,self.b,self.c]

        """
        try:
            while sum(self.angles) != 180:
                print("Angles in a triangle must total 180 degrees, not", sum(self.angles), end='.\n')
                a = input("Please input a new array of angles.\n")
                angles = [int(i) for i in a[1:-1].split(',')]
                self.angles = angles
        except TypeError:
            pass
        """

        self.angles = [self.A, self.B, self.C]
        self.sides = [self.a,self.b,self.c]

        if (None not in self.angles) and (len(self.sides) - self.sides.count(0) == 2):
            if not self.a:
                self.a = cosineRule('a', self.a, self.b, self.c, self.A, self.B, self.C)
            if not self.b:
                self.b = cosineRule('b', self.a, self.b, self.c, self.A, self.B, self.C)
            if not self.c:
                self.c = cosineRule('c', self.a, self.b, self.c, self.A, self.B, self.C)
        if (None not in self.sides):
            if not self.A:
                self.A = cosineRule('A', self.a, self.b, self.c, self.A, self.B, self.C)
            if not self.B:
                self.B = cosineRule('B', self.a, self.b, self.c, self.A, self.B, self.C)
            if not self.C:
                self.C = cosineRule('C', self.a, self.b, self.c, self.A, self.B, self.C)

        self.angles = [self.A, self.B, self.C]
        self.sides = [self.a, self.b, self.c]

        if None not in self.sides:
            self.sideAnalysis = Data(self.sides)

        try:
            if isinstance(self.sideAnalysis.mode[0], int):
                a = self.sides
                while self.sideAnalysis.mode in self.sides:
                    a.remove(self.sideAnalysis.mode)
                base = a[0]
                self.height = pythagoras('hs', self.sideAnalysis.mode[0], base)
            else:
                self.height = None
        except AttributeError:
            self.height = None

        if self.height and base:
            self.area = (base * self.height) / 2
        elif self.a and self.b and self.C:
            self.area = (self.a * self.b * math.sin(self.C)) / 2
        elif self.b and self.c and self.A:
            self.area = (self.b * self.c * math.sin(self.A)) / 2
        elif self.c and self.a and self.B:
            self.area = (self.c * self.a * math.sin(self.B)) / 2
        else:
            self.area = None

        super(self.__class__, self).__init__(self.id, self.sides, self.area)


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

class Square:
    def __init__(self,l1,l2):
        self.length = l1
        self.width = l2
    def diagonal():
        return pythagoras('ss',self.width,self.length)
    def perimiter():
        return 2 * self.length + 2 * self.width

class Data:
    def minDiffFunc(self):
        minDiff = self.maxDiff()
        for i in range(len(self.data)):
            for j in range(1,len(self.data)-i):
                j += i
                temp = self.data[i:j+1]
                if temp[-1] - temp[0] < minDiff and minDiff >= 0:
                    minDiff = temp[-1] - temp[0]
                elif temp[-1] - temp[0] > minDiff and temp[-1] - temp[0] < 0:
                    minDiff = temp[-1] - temp[0]
        return minDiff
    def maxDiffFunc(self):
        maxDiff = 0
        for i in range(len(self.data)):
            for j in range(1,len(self.data)-i):
                j += i
                temp = self.data[i:j+1]
                if temp[-1] - temp[0] > maxDiff:
                    maxDiff = temp[-1] - temp[0]
        return maxDiff

    def modeFunc(self):
        s = []
        max1 = [[]]
        occurences = []
        for i in self.data:
            if i not in s:
                s.append(i)
        for i in s:
            a = self.data.count(i)
            occurences.append(a)
        if occurences.count(sorted(occurences)[-1]) > 1:
            for j in range(len(occurences)):
                if occurences[j] == sorted(occurences)[-1]:
                    max1[0].append(s[j])
            max1.append(sorted(occurences)[-1])
        else:
            max1 = [self.data[occurences.index(sorted(occurences)[-1])],sorted(occurences)[-1]]
        return max1
    
    def medianFunc(self):
        if len(self.data)+1 % 2 == 0:
            return sorted(self.data)[int((len(self.data)+1)/2)-1]
        else:
            return (sorted(self.data)[int((len(self.data))/2)-1] + sorted(self.data)[int((len(self.data)+2)/2)-1])/2
        
    def __init__(self,data):
        self.data = data
        self.range = sorted(self.data)[-1]-sorted(self.data)[0]
        self.mean = sum(self.data)/len(self.data)
        self.mode = self.modeFunc()
        self.median = self.medianFunc()
        self.min = min(self.data)
        self.max = max(self.data)
        self.maxDiff = self.maxDiffFunc()
        self.minDiff = self.minDiffFunc()
    def sumFunc(self):
        return sum(self.data)
    def itemsFunc(self):
        return len(self.data)

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
