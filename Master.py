globals()['__name__'] = 'Functions.py'

def switch(case, *args):
    if not isinstance(args[0],str):
        args = list(*args)
    try:
        case = int(case)
        return args[case -1]
    except (IndexError, TypeError):
        case = input("Invalid input for case. Try again.\n")
        return switch(case,*args)

def advancedSwitch(case,expressions,results):
    newExpressions = [str(case) + ' ' + i for i in expressions]
    evaluation  = [eval(i) for i in newExpressions]
    return results[evaluation.index(True)]
            
def cast(value,dataType):
    if not dataType in ['int','str','list','chr','ord']:
        print('Invalid data type to cast to, please select from:')
        for i in ['int','str','list','chr','ord']:
            print(i)
        dType = input("Please enter a new data type.\n")
        return cast(value,dType)
    try:
        x = eval(dataType + '(' + str(value) + ')')
    except:
        print("Unable to perform cast.")
        return -1
    return x


def printClass(class1):
    for obj in gc.get_objects():
        if isinstance(obj, class1):
            print(obj)
            print(obj.__dict__)


def positions(n):
    a = str(n)[-1]
    if a == 1:
        return a + 'st'
    elif a == 2:
        return a + 'nd'
    elif a == 3:
        return a + 'rd'
    else:
        return a + 'th'

def comma(n):
    temp = list(str(n))
    for i in range(len(temp),0,-3):
        temp.insert(i,',')
    return ''.join(temp[:-1])

def ceasar(phrase,shift): #Ceasar Cipher
    import string
    new = ''
    for i in phrase:
        if i in string.ascii_lowercase:
            new += string.ascii_lowercase[(string.ascii_lowercase.index(i)+2)%len(string.ascii_lowercase)]
        elif i in string.ascii_uppercase:
            new += string.ascii_uppercase[(string.ascii_uppercase.index(i)+2)%len(string.ascii_uppercase)]
        else:
            new += i
    return new

def kwCipher(phrase,kw): #Keyword Cipher
    import string
    alphabet = ''.join([i for i in string.ascii_lowercase if i not in kw])
    key = kw + alphabet
    new = ''
    for i in phrase:
        if i in string.ascii_lowercase:
            new += key[string.ascii_lowercase.index(i)]
        elif i in string.ascii_uppercase:
            new+= key.upper()[string.ascii_uppercase.index(i)]

        else:
            new += i
    return new

#Maths
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

def pythagorasGenerator(m,n):
    for i in range(m,n+m):
        for j in range(m,n+m):
            if (math.sqrt(i**2 + j**2) % 1 == 0) and (j >= i):
                yield (i,j,int(math.sqrt(i**2 + j**2)))

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

def risingFactorial(x,n):
    tot = 1
    for i in range(1,n+2):
        tot *= (x + i-1)
    return tot

def fallingFactorial(x,n):
    tot = 1
    for i in range(1,n+1):
        tot *= (x - (i-1))
    return tot

def factorial(x):
    return fallingFactorial(x,x)

def combinations(n,r):
    return permutations(n,r)/factorial(r)

def permutations(n,r):
    return factorial(n)/factorial(n-r)

def quadratic(a,b,c):
    solutions = [(-b + math.sqrt(b**2 - 4*a*c))/2*a,(-b - math.sqrt(b**2 - 4*a*c))/2*a]
    return solutions

def distance(x1,x2,y1,y2):
    return math.sqrt(((y2-y1)**2)+((x2-x1)**2))

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

def inverseSin(x):
    return math.asin(x*(math.pi/180))

def inverseCos(x):
    return math.asin(x*(math.pi/180))

def inverseTan(x):
    return math.atan(x*(math.pi/180))

def USInflate(money,fromMonth,fromYear,toMonth=0,toYear=0):
    import pip
    import importlib

    pkgs = ['requests','bs4','mechanicalsoup']
    for package in pkgs:
        try:
            importlib.__import__(package)
        except ImportError as e:
            pip.main(['install', package])

    import mechanicalsoup
    import time
    address = "https://data.bls.gov/cgi-bin/cpicalc.pl"
    months = ['January','February','March','April','May','June','July','August','September','October','Novemeber','December']
    getNewDate = mechanicalsoup.StatefulBrowser()
    getNewDate.open(address)
    getNewDate = getNewDate.select_form('form')
    getNewDate = getNewDate.form.find_all('option')
    getNewDate = getNewDate[-1].attrs['value']
    if toMonth == 0:
        toMonth = getNewDate[-2:]
    if toYear == 0:
        toYear = int(getNewDate[:-2])
    elif isinstance(toMonth,str)and len(toMonth) > 2:
        try:
            toMonth = months.index(toMonth)+1
        except ValueError:
            toMonth = time.strftime('%m')
    if isinstance(fromMonth,str) and len(fromMonth) > 2:
        try:
            fromMonth = months.index(fromMonth)+1
        except ValueError:
            fromMonth = time.strftime('%m')
    while toMonth > int(getNewDate[-2:]) and toYear == int(getNewDate[:-2]):
        toMonth = input('Please enter a different month, as data for', months[int(toMonth)-1], 'of', int(getNewDate[:-2]), 'is unavailable.\n')
    while toYear < 1913 or toYear > int(getNewDate[:-2]):
        toYear = input("Final year out of range (1913-2017), please enter a new value.\n")
    while fromYear < 1913 or fromYear > int(getNewDate[:-2]):
        fromYear = input("Initial year out of range (1913-2017), please enter a new value.\n")
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(address)
    browser2 = browser.select_form('form')
    browser2.set('cost1',money)
    browser2.set('year1',str(fromYear) + fromMonth)
    browser2.set('year2', str(toYear) + toMonth)
    resp = browser.submit_selected()

    browser2 = browser.select_form('form')
    result = str(browser2.form.find_all('span')).replace('[<span id="answer">',"").replace('</span>]',"")
    print('$' + str(money),'in',months[int(fromMonth)-1],'of',fromYear,'is worth', result, 'in',months[int(toMonth)-1],'of',toYear,end='.')


def baseConvert(num, base1, base2):
    import math
    import string

    accepted = True
    base10Nums = []
    baseStr = ""

    digits = [str(i) for i in list(range(0, 10))]
    digits.extend(list(string.ascii_uppercase))
    digits.extend(list(string.ascii_lowercase))
    digits.extend(['+', '/'])

    if any(num not in digits for num in list(str(num))):
        numRedo = input(
            'Unsupported characters in inputted number. The allowed characters are:\n' + str(digits).replace('\'','').replace(
                '[', '').replace(']', '') + '\nPlease enter a new number.\n')
        accepted = False

    if any(x > 64 and x < 2 for x in [base1,base2]):
        base1Redo, base2Redo = input(
            'Base(s) inputted invalid, the largest accepted base is base 64, and the smallest is base 2. Please input your two bases again, space separated. ({Base1} {Base2})\n').split()
        accepted = False

    if not accepted:
        baseConvert(numRedo, base1Redo, base2Redo)

    for i in range(len(str(num))):
        base10Nums.append((base1 ** (len(str(num)) - (i + 1))) * digits.index(str(num)[i]))

    newNum = sum(base10Nums)

    if base2 == 10:
        return newNum

    a = math.floor(math.log(newNum, base2))

    for i in range(a, -1, -1):

        if newNum // base2 ** i <= base2 - 1:
            baseStr += str(newNum // base2 ** i)
            newNum -= (newNum // base2 ** i) * (base2 ** i)

        else:
            baseStr += "0"

    return baseStr
