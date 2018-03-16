def mod(b,a):
    return b - a*int(b/a)

def  powerGen(m=2,n=-2):
    count = -1
    while count >= n:
        count += 1
        yield count**m

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
def sin(x):
    x = x / (180/3.1415926535897)
    n = 100
    valid = False
    while valid != True:
        valid = True
        ret = 0
        try:
            for i in range(n):
                ret += ((-1)**(i) * (x)**(2*i +1))/(factorial(2*i + 1))
        except OverflowError:
            n -= 1
            valid = False
    return ret

def cos(x):
    return sin(90-x)

def tan(x):
    return sin(x) / cos(x)
