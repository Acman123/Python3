class Data:
    def minDiffFunc(self):
        minDiff = self.maxDiff()
        for i in range(len(self.data)):
            for j in range(1,len(self.data)-i):
                j += i
                temp = self.data[i:j+1]
                if temp[-1] - temp[0] < minDiff and minDiff >= 0:
                    minDiff = temp[-1] - temp[0]
                elif temp[-1] - temp[0] > minDiff and temp[-1] - temp[0] < 0:
                    minDiff = temp[-1] - temp[0]
        return minDiff
    def maxDiffFunc(self):
        maxDiff = 0
        for i in range(len(self.data)):
            for j in range(1,len(self.data)-i):
                j += i
                temp = self.data[i:j+1]
                if temp[-1] - temp[0] > maxDiff:
                    maxDiff = temp[-1] - temp[0]
        return maxDiff

    def modeFunc(self):
        s = []
        max1 = [[]]
        occurences = []
        for i in self.data:
            if i not in s:
                s.append(i)
        for i in s:
            a = self.data.count(i)
            occurences.append(a)
        if occurences.count(sorted(occurences)[-1]) > 1:
            for j in range(len(occurences)):
                if occurences[j] == sorted(occurences)[-1]:
                    max1[0].append(s[j])
            max1.append(sorted(occurences)[-1])
        else:
            max1 = [self.data[occurences.index(sorted(occurences)[-1])],sorted(occurences)[-1]]
        return max1
    
    def medianFunc(self):
        if len(self.data)+1 % 2 == 0:
            return sorted(self.data)[int((len(self.data)+1)/2)-1]
        else:
            return (sorted(self.data)[int((len(self.data))/2)-1] + sorted(self.data)[int((len(self.data)+2)/2)-1])/2
        
    def __init__(self,data):
        self.data = data
        self.range = sorted(self.data)[-1]-sorted(self.data)[0]
        self.mean = sum(self.data)/len(self.data)
        self.mode = self.modeFunc()
        self.median = self.medianFunc()
        self.min = min(self.data)
        self.max = max(self.data)
        self.maxDiff = self.maxDiffFunc()
        self.minDiff = self.minDiffFunc()
    def sumFunc(self):
        return sum(self.data)
    def itemsFunc(self):
        return len(self.data)
