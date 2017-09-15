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

def heronsFomula():
    pass

#Trigonometry
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
