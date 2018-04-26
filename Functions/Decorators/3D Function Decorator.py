class Func3D():
    def __init__(self, func):
        self.f = func
        self.xos = 0
        self.yos = 0
        self.zos = 0
        
    def __call__(self,x,y):
        return self.f(x,y)

    def offSet(self, xos=0, yos=0, zos=0):
        self.xos = xos
        self.yos = yos
        self.zos = zos

        def __call__(x, y):
            return self.f(x-self.xos, y-self.yos) + self.zos

        return __call__
