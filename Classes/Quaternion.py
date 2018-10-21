import math

class Quaternion:
    def __init__(self,re,i,j,k):
        self.re = re
        self.i = i
        self.j = j
        self.k = k
        self.magnitude = math.sqrt(sum(map(lambda x: x**2,[self.re,self.i,self.j,self.k])))

    def conjugate(self):
        return Quaternion(self.re, -1 * self.i, -1 * self.j, -1 * self.k)

    def verser(self):
        return self / self.magnitude

    def __repr__(self):
        vals = [self.re, self.i, self.j, self.k]
        end = ["", "i", "j", "k"]
        ret = ""
        for i in range(len(vals)):
            if vals[i] != 0:
                if vals[i] == 1:
                    ret += end[i]
                elif vals[i] == -1:
                    ret += "-" + end[i]
                else:
                    ret += f"{vals[i]:.1f}" + end[i]
                if i != 3:
                    ret += " + "
        return ret

    def __add__(self,other):
        newRe = self.re + other.re
        newI = self.i + other.i
        newJ = self.j + other.j
        newK = self.k + other.k
        return Quaternion(newRe,newI,newJ,newK)

    def __sub__(self,other):
        return self + -1 * other

    def __mul__(self, other):
        newRe = self.re * other.re - self.i * other.i - self.j * other.j - self.k * other.k
        newI = self.i * other.re + self.re * other.i + self.j * other.k - self.k * other.j
        newJ = self.re * other.j + self.j * other.re + self.k * other.i - self.i * other.k
        newK = self.k * other.re - self.j * other.i + self.i * other.j + self.re * other.k
        return Quaternion(newRe,newI,newJ,newK)

    def __rmul__(self,other):
        newRe = other * self.re
        newI = other * self.i
        newJ = other * self.j
        newK = other * self.k
        return Quaternion(newRe,newI,newJ,newK)

    def __truediv__(self,other):

        if isinstance(other,Quaternion):
            pass
            newRe = self.re * other.re - self.i * other.i - self.j * other.j - self.k * other.k
            newI = self.i * other.re + self.re * other.i + self.j * other.k - self.k * other.j
            newJ = self.re * other.j + self.j * other.re + self.k * other.i - self.i * other.k
            newK = self.k * other.re - self.j * other.i + self.i * other.j + self.re * other.k

        elif isinstance(other,(int, float)):
            return 1/other * self

        else:
            raise TypeError

        return Quaternion(newRe,newI,newJ,newK)

    def __pow__(self, power):
        if power > 2:
            return self * self**(power-1)
        return self * self

    def inverse(self):
        return self.conjugate() / (self.magnitude**2)
