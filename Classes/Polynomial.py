class Polynomial():
    def __init__(self,*coeffs,var="x"):
        self.coeffs = coeffs
        self.var = "x"

    def __call__(self,x):
        return self.func()(x)

    def __repr__(self):
        rep = ""
        for i in range(len(self.coeffs)):
            if self.coeffs[i] == 0:
                continue

            if rep == "":
                if i + 1 == len(self.coeffs):
                    return str(self.coeffs[i])
                
                if self.coeffs[i] in [1, -1]:
                    rep += str(self.coeffs[i]).replace('1','')

                else:
                    rep += f"{self.coeffs[i]}"

            else:
                if self.coeffs[i] > 0:
                    rep += " + "

                else:
                    rep += " - "

                if self.coeffs[i] not in [1,-1] or i + 1 == len(self.coeffs):
                    rep += str(abs(self.coeffs[i]))

            if i + 2 == len(self.coeffs):
                rep += self.var

            elif i + 1 != len(self.coeffs):
                rep += self.var + f"^{len(self.coeffs) - i - 1}"

        return rep
    
    def __add__(self,other):
        return Polynomial(*(x + y for x,y in zip(self.coeffs,other.coeffs)))

    def __sub__(self,other):
        return Polynomial(*(x - y for x,y in zip(self.coeffs,other.coeffs)))

    def __mul__(self,other):
        coeffs = []
        for i in range(len(self) + len(other) + 2):
            coeffs.append(0)

        selfCoeffs = list(reversed(self.coeffs))
        otherCoeffs = list(reversed(other.coeffs))
        for i in range(len(self)+1):
            for j in range(len(other)+1):
                coeffs[i + j] += selfCoeffs[i] * otherCoeffs[j]

        return Polynomial(*tuple(reversed(coeffs)))
    
    def __rmul__(self, other):
        self.coeffs = [i * other for i in self.coeffs]
        return self

    def __pow__(self,power):
        if power == 1:
            ret = self
        else:
            ret = self * pow(self, power-1)
        return ret

    def __len__(self):
        for i in range(len(self.coeffs)):
            if self.coeffs[i] != 0:
                return len(self.coeffs) - i - 1

    def func(self):
        return lambda x:eval(self.__repr__.replace("x",str(x)))
