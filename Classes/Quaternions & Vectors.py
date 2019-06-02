import math

class Vector:
    def __init__(self, *args):
        self.components = args

    def dotProduct(self, other):
        return sum([i * j for i, j in zip(self,components, other.components)])

    def __mul__(self, other):
        return self.dotProduct(other)

    def __add__(self,other):
        return self.__class__(*[i + j for i, j in zip(self.components, other.components)])

    def __sub__(self,other):
        return self + -1 * other

    @property
    def magnitude(self):
        return math.sqrt(sum(map(lambda x: x**2,self.components)))

    def __eq__(self, other):
        if isinstance(other, Vector3):
            other = other.quaternion

        elif isinstance(other,(int, float)):
            other = Quaternion(other, 0,0,0)

        if isinstance(other,Quaternion):
            return self.re == other.re and self.vector == self.vector

        else:
            raise TypeError

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other,(Quaternion, Vector3)):
            return self.magnitude < other.magnitude

        if isinstance(other,(int, float)):
            return self.magnitude < other
        
        else:
            raise TypeError


    def __le__(self, other):
        return self < other or self.magnitude == other.magnitude

    def __lt__(self, other):
        if isinstance(other,Vector):
            return self.magnitude > other.magnitude

        if isinstance(other,(int, float)):
            return self.magnitude > other
        
        else:
            raise TypeError


    def __ge__(self, other):
        return self > other or self.magnitude == other.magnitude

    def __getitem__(self, pos):
        return self.components[pos]

    def __len__(self):
        return self.magnitude


class Vector3(Vector):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.components = [self.x,self.y,self.z]
        super().__init__(*self.components)

    @property
    def quaternion(self):
        if isinstance(self, Quaternion):
            return self
        print(self.components)
        return Quaternion(0, *self.components)

    def crossProduct(self, other):
        newX = self[1] * other[2] - self[2] * other[1]
        newY = self[2] * other[0] - self[0] * other[2]
        newZ = self[0] * other[1] - self[1] * other[0]
        return Vector3(newX, newY, newZ)

    def __matmul__(self,other):
        return self.crossProduct(other)

    def __pow__(self, power):
        if power > 2:
            return self @ self**(power-1)
        return self @ self

class Quaternion(Vector3):
    def __init__(self,re = 1,i = 0,j = 0,k = 0):
        self.re = re
        self.i = i
        self.j = j
        self.k = k
        self.vector = Vector3(self.i, self.j, self.k)
        super().__init__(*self.vector.components)
        self.components = [self.re, *self.vector.components]

    @property
    def conjugate(self):
        return Quaternion(self.re, -1 * self.i, -1 * self.j, -1 * self.k)

    @property
    def inverse(self):
        return self.conjugate / (self.magnitude**2)

    @property
    def verser(self):
        return self / self.magnitude

    def __pow__(self, power):
        if power > 2:
            return self * self**(power-1)
        return self * self

    def __repr__(self):
        """
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
        """

        return "[{} ({} {} {})]".format(*self.components)


    def __mul__(self, other):
        if isinstance(other, Vector3):
            other = other.quaternion

        if isinstance(other,Quaternion):
            newRe = self.re * other.re - self.i * other.i - self.j * other.j - self.k * other.k
            newI = self.i * other.re + self.re * other.i + self.j * other.k - self.k * other.j
            newJ = self.re * other.j + self.j * other.re + self.k * other.i - self.i * other.k
            newK = self.k * other.re - self.j * other.i + self.i * other.j + self.re * other.k
            return Quaternion(newRe,newI,newJ,newK)

        elif isinstance(other,(int, float)):
            return Quaternion(*[i * other for i in self.compoents])

        else:
            raise TypeError

    def __truediv__(self,other):
        if isinstance(other, Vector3):
            other = other.quaternion

        elif isinstance(other,(int, float)):
            other = Quaternion(other, 0, 0, 0)
        
        if isinstance(other,Quaternion):
            return self * other.inverse

        else:
            raise TypeError
