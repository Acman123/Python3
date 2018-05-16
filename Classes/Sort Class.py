class Sort():
    def __init__(self,array):
        self.l = array
        self.len = len(array)

    def timeit(method):
        import time
        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            timed = (te - ts) * 1000
            print("{} took {:.2f}ms to run.".format(method.__name__,timed))
            return result
        return timed

    @timeit
    def insertionSort(self):
        array = self.l   
        for i in range(1,len(array)):
            for j in range(0,i):
                if array[i] <= array[j]:
                    temp = array[i]
                    del array[i]
                    array.insert(j,temp)
        self.sorted = array
        return self.sorted

    @timeit
    def bubbleSort(self):
        array = self.l
        for i in range(len(array)):
            for j in range(len(array)-i):
                if array[i-1] > array[i] and i > 0:
                    temp = array[i]
                    array[i] = array[i-1]
                    array[i-1] = temp
        self.sorted = array
        return self.sorted

    def mergeSort(self):
        array = self.l
        pass

    def sortAll(self):
        sorts = [self.insertionSort,self.bubbleSort, self.mergeSort]
        for i in range(len(sorts)):
            print(sorts[i](),'\n')
