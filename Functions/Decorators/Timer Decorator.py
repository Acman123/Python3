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
