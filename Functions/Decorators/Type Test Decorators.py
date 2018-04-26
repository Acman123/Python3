def intTest(f):
    def helper(x):
        if isinstance(x,int):
            return f(x)
        else:
            raise ValueError("Argument is not an integer")
    return helper

def realTest(f):
    def helper(x):
        if isinstance(x,float):
            return f(x)
        else:
            raise ValueError("Argument is not an real")
    return helper

def strTest(f):
    def helper(x):
        if isinstance(x,str):
            return f(x)
        else:
            raise ValueError("Argument is not a string")
    return helper

def arrayTest(f):
    def helper(x):
        if isinstance(x,list):
            return f(x)
        else:
            raise ValueError("Argument is not an array")
    return helper

def posTestWith0(f):
    def helper(x):
        if x >= 0:
            return f(x)
        else:
            raise ValueError("Argument is not positive or zero")
    return helper

def posTest(f):
    def helper(x):
        if x > 0:
            return f(x)
        else:
            raise ValueError("Argument is not positive")
    return helper

def negTestWith0(f):
    def helper(x):
        if x <= 0:
            return f(x)
        else:
            raise ValueError("Argument is not negative or zero")
    return helper

def negTest(f):
    def helper(x):
        if x < 0:
            return f(x)
        else:
            raise ValueError("Argument is not negative")
    return helper
