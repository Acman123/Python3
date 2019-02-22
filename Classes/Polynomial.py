class Polynomial():
    def __init__(self,*coeffs):
        self.coeffs = coeffs

    def __call__(self,x):
        return self.func()(x)

    def __repr__(self):
        rep = ""
        for i in range(len(self.coeffs)):
            if self.coeffs[i] == 0:
                continue

            elif i + 1 == len(self.coeffs):
                rep += f'{self.coeffs[i]}'
                break

            elif self.coeffs[i] == 1:
                if i + 2 == len(self.coeffs):
                    rep += f'x'

                else:
                    rep += f'x^{len(self.coeffs) - i - 1}'
            else:
                if i + 2 == len(self.coeffs):
                    rep += f'{self.coeffs[i]}x'
                else:
                    rep += f'{self.coeffs[i]}x^{len(self.coeffs) - i - 1}'

            if i + 1 != len(self.coeffs) and sum([x if x > 0 else -x for x in self.coeffs[i + 1:]]) > 0:
                rep += " + "
        return rep

    def funcRepr(self):
        rep = ""
        for i in range(len(self.coeffs)):
            if self.coeffs[i] == 0:
                continue

            elif i + 1 == len(self.coeffs):
                rep += f'{self.coeffs[i]}'
                break

            elif self.coeffs[i] == 1:
                if i + 2 == len(self.coeffs):
                    rep += f'x'

                else:
                    rep += f'x^{len(self.coeffs) - i - 1}'
            else:
                if i + 2 == len(self.coeffs):
                    rep += f'{self.coeffs[i]}*x'
                else:
                    rep += f'{self.coeffs[i]}*x**{len(self.coeffs) - i - 1}'

            if i + 1 != len(self.coeffs) and sum([x if x > 0 else -x for x in self.coeffs[i + 1:]]) > 0:
                rep += " + "
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
        return lambda x:eval(self.funcRepr().replace("x",str(x)))
