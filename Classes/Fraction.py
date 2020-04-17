class Fraction:
    def __init__(self, p,q=1):
        self.p = p # Top
        self.q = q # Bottom

        self.simplify()

    def __add__(self, other):
        return Fraction(self.p * other.q + self.q * other.p, other.q * self.q).simplify()

    def __sub__(self, other):
        return self + (-1 * other)

    def __mul__(self, other):
        return Fraction(self.p * other.p, self.q * other.q).simplify()

    def __rmul__(self, other):
        return Fraction(other,1).simplify() * self

    def __repr__(self):
        return f"{self.p}/{self.q}"

    def simplify(self):
        if self.q != 1:
            g = gcd(self.p, self.q)
            self.p //= g
            self.q //= g
            
        else:
            if type(self.p) == float:
                p = str(self.p)
                d = len(p[p.find(".")+1:])
                f = Fraction(int(self.p * 10**d), 10**d).simplify()            
                self.p = f.p
                self.q = f.q

            elif type(self.p) == str:
                #Total digits before repeat
                d1 = len(self.p[self.p.find(".")+1:]) - 2 # Minus 2 for the brackets

                #Digits before recurring bit
                d2 = len(self.p[self.p.find(".")+1:self.p.find("(")])

                # When we multiply by our power of ten we will have no decimals after float1 or float2
                # This is because they are the repeating parts, and when we subtract then the recurring part will go
                # So we exclude them as it makes no difference to the actual calculation and lets us avoid actually implementing recurring decimals
                float1 = self.p.replace("(","").replace(")","")
                float2 = self.p[:self.p.find("(")]
                final = 10**d1 * float(float1) - 10**d2 * float(float2)
                
                f = Fraction(int(final), 10**d1 - 10**d2).simplify()
                self.p = f.p
                self.q = f.q
        return self
