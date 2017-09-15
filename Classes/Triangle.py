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

class Polygon(object):
    def __init__(self,id1,sides,area):
        self.id = id1
        self.noSides = len(sides)
        self.area = area
        self.sides = sides
        if None not in sides:
            self.perimeter = sum(sides)

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
       
def pythagoras(mode,l1,l2):
    if not mode in ['ss','hs','sh']:
        print('Invalid mode, please select from:')
        for i in ['ss - Two sides', 'hs or sh - Hypotanuse and side']:
            print(i)
        mode = input("Please choose a new mode.\n")
        return pythagoras(mode,l1,l2)
    elif mode == 'ss':
        return math.sqrt(l1**2 + l2**2)
    elif mode == 'hs':
        new = sorted([l1,l2])
        return math.sqrt((new[1]**2)-(new[0]**2))
    elif mode == 'sh':
        new = sorted([l1,l2])
        return math.sqrt((new[0]**2)-(new[1]**2))
    else:
        return -1
      
def cosineRule(mode,a,b,c,A,B,C):
    w = []
    if a == 0:
        a = None
    if b == 0:
        b = None
    if c == 0:
        c = None
    if A in [0,None]:
        A = None
    else:
        A = A/(180/math.pi)
    if B in [0,None]:
        B = None
    else:
        B = B/(180/math.pi)
    if C in [0,None]:
        C = None
    else:
        C = C/(180/math.pi)
    if 'a' in mode:
        w.append(('a',math.sqrt(b**2 + c**2 - (2*b*c*math.cos(A)))))
    if 'b' in mode:
        w.append(('b',math.sqrt(a**2 + c**2 - (2*a*c*math.cos(B)))))
    if 'c' in mode:
        w.append(('c',math.sqrt(b**2 + a**2 - (2*b*a*math.cos(C)))))
    if 'A' in mode:
        x = ((b**2+c**2)-a**2)/(2*b*c)
        z = str(x).split('.')[0]
        y = len(''.join(z))
        if z == '0':
            y = 0
        w.append(('A',math.acos(x/(10**y))*180/math.pi))

    if 'B' in mode:
        x = ((a**2+c**2)-b**2)/(2*a*c)
        z = str(x).split('.')[0]
        y = len(''.join(z))
        if z == '0':
            y = 0
        w.append(('B',math.acos(x/(10**y))*180/math.pi))
        
    if 'C' in mode:
        x = ((b**2+a**2)-c**2)/(2*b*a)
        z = str(x).split('.')[0]
        y = len(''.join(z))
        if z == '0':
            y = 0
        w.append(('C',math.acos(x/(10**y))*180/math.pi))
    return w

def sineRule(mode,a,b,c,A,B,C):
    x = []
    if a == 0:
        a = None
    if b == 0:
        b = None
    if c == 0:
        c = None
    if A == 0:
        A = None
    else:
        A = A/(180/math.pi)
    if B == 0:
        B = None
    else:
        B = B/(180/math.pi)
    if C == 0:
        C = None
    else:
        C = C/(180/math.pi)
    if ('a' in mode) and (b and B) and A:
        print('1')
        x.append(('a', (b*math.sin(A)/math.sin(B))))
    if ('a' in mode) and (c and c) and A and (not any('a' in sublist for sublist in x)):
        print('2')
        x.append(('a', (c*(math.sin(A))/math.sin(C))))
    if ('b' in mode) and (c and C) and B:
        print('3')
        x.append(('b', (c*math.sin(B)/math.sin(C))))
    if ('b' in mode) and (a and A) and B and (not any('b' in sublist for sublist in x)):
        print('4')
        x.append(('b', (a*math.sin(B)/math.sin(A))))
    if ('c' in mode) and (b and B) and C:
        print('5')
        x.append(('c', (b*math.sin(C)/math.sin(B))))
    if ('c' in mode) and (a and A) and C and (not any('c' in sublist for sublist in x)):
        print('6')
        x.append(('c', (a*math.sin(C)/math.sin(A))))
    return x

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return sin(x)/cos(x)
