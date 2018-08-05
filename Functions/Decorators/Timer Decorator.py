import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        timed = (te - ts) * 1000
        print("{} took {:.2f}ms to run.".format(method.__name__,timed))
        return result
    return timed

def avgTimeit(method,n):
    def timed(*args, **kw):
        values = []
        for i in range(n):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            timed = (te - ts) * 1000
            values.append(timed)

        valuesRange = max(values) - min(values)
        avg = sum(values)/n
        print("{} took {:.2f}ms to run, with a range of {:.2f}ms.".format(method.__name__, avg, valuesRange))
        return result
    return timed
