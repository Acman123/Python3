class Func2D():
    def __init__(self, func):
        self.f = func
        self.xos = 0
        self.yos = 0
        
    def __call__(self,x):
        return self.f(x)

    def offSet(self, xos=0, yos=0):
        self.xos = xos
        self.yos = yos

        def __call__(self,x):
            return self.f(x-self.xos) + self.yos

        return __call__
