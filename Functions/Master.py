import cmath
import math
import gc


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
