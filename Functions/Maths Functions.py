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
