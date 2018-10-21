import math

class Complex:
    def __init__(self,re,i):
        self.re = re
        self.i = i
        self.magnitude = math.sqrt(sum(map(lambda x: x**2,[self.re,self.i])))

    def conjugate(self):
        return Complex(self.re, -1 * self.i)

    def unit(self):
        return self / self.magnitude

    def __repr__(self):
        vals = [self.re, self.i]
        end = ["", "i"]
        ret = ""
        for i in range(len(vals)):
            if vals[i] != 0:
                if vals[i] == 1:
                    ret += end[i]
                elif vals[i] == -1:
                    ret += "-" + end[i]
                else:
                    ret += f"{vals[i]:.1f}" + end[i]
                if i != 1:
                    ret += " + "
        return ret

    def __add__(self,other):
        newRe = self.re + other.re
        newI = self.i + other.i
        return Complex(newRe,newI)

    def __sub__(self,other):
        return self + -1 * other

    def __mul__(self, other):
        newRe = self.re * other.re - self.i * other.i
        newI = self.re * other.i + self.i * other.i
        return Complex(newRe,newI)

    def __rmul__(self,other):
        newRe = other * self.re
        newI = other * self.i
        return Complex(newRe,newI)

    def __truediv__(self,other):
        if isinstance(other,Complex):
            return self * other.inverse()

        elif isinstance(other,(int, float)):
            return 1/other * self

        else:
            raise TypeError

    def __pow__(self, power):
        if power > 2:
            return self * self**(power-1)
        return self * self

    def inverse(self):
        return self.conjugate() / (self.magnitude**2)
