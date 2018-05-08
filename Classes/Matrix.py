class Matrix:
    def __init__(self,*args):
        self.matrix = list(args)
        self.rows = len(self.matrix)

        cols = len(self.matrix[0])
        for i in range(1,len(self.matrix)):
            if len(self.matrix[i]) != cols:
                raise Exception("Rows of different length entered.")

        self.columns = cols

    def multChecker(f):
        def wrapper(*args):
            self = list(args)[0]
            other = list(args)[1]
            if self.columns != other.rows:
                raise Exception(f"Two matrices can only {f.__doc__} if the number of columns of the first matrix is equal to the number of rows in the second.")
            return f(*args)
        return wrapper

    def squareChecker(f):
        def wrapper(*args):
            self = list(args)[0]
            if self.rows != self.colums:
                raise Exception(f"Non-square matrices cannot be {f.__doc__}.")
            return f(*args)
        return wrapper

    def sameSizeCheck(f):
        def wrapper(*args):
            self = list(args)[0]
            other = list(args)[1]
            if other.rows != self.rows or other.columns != self.columns:
                raise Exception(f"Matrices of different sizes cannot be {f.__doc__}.")
            return f(*args)
        return wrapper

    @sameSizeCheck
    def __add__(self,other):
        '''added'''
        newMatrix = []
        for i in range(self.rows):
            newMatrix.append([self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)])
        return Matrix(*newMatrix)

    @sameSizeCheck
    def __sub__(self,other):
        '''subtracted'''
        newMatrix = []
        for i in range(self.rows):
            newMatrix.append([self.matrix[i][j] - other.matrix[i][j] for j in range(self.columns)])
        return Matrix(*newMatrix)

    @multChecker
    def __mul__(self,other):
        """multiplied"""
        newMatrix = []
        for i in range(self.rows):
            newMatrix.append([sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns)]) for j in range(other.columns)])
        return Matrix(*newMatrix)

    def __pow__(self,power):
        if power == 2:
            ret = self * self
        elif power == 1:
            ret = self
        else:
            ret = self * pow(self, power-1)
        return ret
        
    def __repr__(self):
        containerStr = str(self.matrix)[1:-1]
        for i in range(len(containerStr)-containerStr.count(',')+self.rows-1):
            if containerStr[i-1] in ['0','1','2','3','4','5','6','7','8','9'] and containerStr[i] == ',':
                containerStr = list(containerStr)
                del containerStr[i]
                containerStr = ''.join(containerStr)
                
        minPoint = 0
        maxPoint = 0
        notFirst = 0
        retStr = ""
        for i in range(len(containerStr)):
            try:
                if containerStr[i] == ']' and containerStr[i+1] == ',':
                    maxPoint = i+2
                    retStr += containerStr[minPoint+notFirst:maxPoint-1] + '\n'
                    notFirst = 1
                    minPoint = i+2
            except IndexError:
                retStr += containerStr[minPoint+1:]
            

        return retStr
