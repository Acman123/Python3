import math

def positions(n):
    n = str(n)
    a = n[-1]
    if a == "1":
        return n + 'st'
    elif a == "2":
        return n + 'nd'
    elif a == "3":
        return n + 'rd'
    else:
        return n + 'th'

def checkPrime(n):
    prime = n
    absolute = True
    posibility = True
    isPrime = False
    for i in range(2,int(math.sqrt(prime))+1):
        check = prime/i
        if check.is_integer():
            absolute = False
        else:
            posibility = True
    if posibility and absolute:
        isPrime = True
    return isPrime

def genPrime(num=None):
    prime = 1
    allp = []
    check = 0
    absolute = True
    posibility = True
    x = 0

    try:
        try:
            count = 1
            while count <= num:
                prime = prime+1
                absolute = True
                posibility = True
                if len(allp) > 0:
                    latestPrime = allp[-1]
                else:
                    latestPrime = 0
                if checkPrime(prime):
                    allp.insert(x,prime)
                    x+=1
                if latestPrime == allp[-1]:
                    continue
                count += 1
                yield allp[-1]
            raise StopIteration
                
        except TypeError:
            while True:
                prime = prime+1
                absolute = True
                posibility = True
                if len(allp) > 0:
                    latestPrime = allp[-1]
                else:
                    latestPrime = 0
                if checkPrime(prime):
                    allp.insert(x,prime)
                    x+=1
                if latestPrime == allp[-1]:
                    continue
                yield allp[-1]

    except StopIteration:
        print("The {} prime is: {}.".format(positions(num),allp[-1]))
