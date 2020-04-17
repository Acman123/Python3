class Fraction:
    def __init__(self, p,q=1):
        self.p = p # Top
        self.q = q # Bottom

        self.simplify()

    def __add__(self, other):
        return Fraction(self.p * other.q + self.q * other.p, other.q * self.q)

    def __radd__(self, other):
        return Fraction(other,1) + self

    def __sub__(self, other):
        return self + (-1 * other)

    def __mul__(self, other):
        try:
            return Fraction(self.p * other.p, self.q * other.q)
        except:
            return self.__rmul__(other)

    def __rmul__(self, other):
        return Fraction(other,1) * self

    def __repr__(self):
        return f"{self.p}/{self.q}" if self.q != 1 else str(self.p)

    def __str__(self):
        return f"{self.p}/{self.q}" if self.q != 1 else str(self.p)
    
    def __gt__(self,other):
        if type(other).__name__ != "Fraction":
            o = Fraction(other)
        return self.p * o.q > self.q * o.p

    def __ge__(self,other):
        if type(other).__name__ != "Fraction":
            o = Fraction(other)
        return self.p * o.q >= self.q * o.p        

    def __lt__(self, other):
        if type(other).__name__ != "Fraction":
            o = Fraction(other)
        return self.p * o.q < self.q * o.p

    def __le__(self,other):
        if type(other).__name__ != "Fraction":
            o = Fraction(other)
        return self.p * o.q <= self.q * o.p     

    def __eq__(self,other):
        if type(other).__name__ != "Fraction":
            o = Fraction(other)
        return self.q * o.p == self.p * o.q

    def __ne__(self,other):
        if type(other).__name__ != "Fraction":
            o = Fraction(other)
        return self.q * o.p != self.p * o.q

    def __abs__(self):
        return Fraction(abs(self.p), self.q)

    def simplify(self):
        if self.q != 1:
            g = gcd(abs(self.p), abs(self.q))
            self.p //= g
            self.q //= g
            if self.q < 0:
                self.q = -1 * self.q
                self.p = -1 * self.p
            
        else:
            if type(self.p) == float:
                p = str(self.p)
                d = len(p[p.find(".")+1:])
                f = Fraction(int(self.p * 10**d), 10**d).simplify()            
                self.p = f.p
                self.q = f.q

            elif type(self.p) == str:
                if "(" in self.p:
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
                    
                    f = Fraction(int(final), 10**d1 - 10**d2)
                    self.p = f.p
                    self.q = f.q

                elif "/" in self.p:
                    fParts = self.p.split("/")
                    f = Fraction(int(fParts[0]), int(fParts[1]))
                    self.p = f.p
                    self.q = f.q

                elif "." in self.p:
                    d = len(self.p[self.p.find(".")+1:])
                    p = float(self.p) * 10**d
                    q = 10**d
                    f = Fraction(int(p), q)
                    self.p = f.p
                    self.q = f.q

                else:
                    self.p = int(self.p)
                    self.q = 1

        return self
