class PriorityQueue(object):
    """
    Max PriorityQueue
    Binary heap based implementation
    """

    def __init__(self):
        self.data = []

    def insert(self,d):
        self.data.append(d)
        self.__siftup()

    def extractMax(self):
        max = -1

        if not len(self.data) == 0:
            max = self.data[0]
        
        self.__siftdown()
        return max

    def __siftup(self):
        index = len(self.data) - 1
        pIndex = (index - 1)/2

        while pIndex >= 0 and self.data[index] > self.data[pIndex]:
            self.data[pIndex], self.data[index] = self.data[index], self.data[pIndex]
            index = pIndex
            pIndex = (index - 1)/2

    def __siftdown(self):
        self.data[0] = self.data.pop()
        index = 0

        while index *2 <= len(self.data) -2:
            maxIndex = self.__getMaxIndex(index)
            if self.data[maxIndex] > self.data[index]:
                self.data[maxIndex], self.data[index] = self.data[index], self.data[maxIndex]
                index = maxIndex
            else:
                break

    def __getMaxIndex(self,i):
        lIndex = i*2 +1
        rIndex = lIndex + 1
        
        if rIndex >= len(self.data) or self.data[lIndex] > self.data[rIndex]:
            return lIndex
        else:
            return rIndex

"""Test Script"""

q = PriorityQueue()
q.insert(3)
q.insert(6)
q.insert(2)
q.insert(4)
q.insert(9)
q.insert(5)
q.insert(7)
q.insert(1)
print q.extractMax()
print q.extractMax()
print q.extractMax()
print q.extractMax()
