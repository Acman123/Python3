def iterator(f):
    
    def iterate(n, jump = 1, limit = True):
        while n <= limit if limit != True else limit:
            yield f(n)
            n += jump
    
    return iterate
