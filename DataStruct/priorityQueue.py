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

        while pIndex > 0 and self.data[pIndex] > self.data[index]:
            self.data[pIndex], self.data[index] = self.data[index], self.data[pIndex]
            index = pIndex
            pIndex = (index - 1)/2

    def __siftdown(self):
        self.data[0] = self.data.pop()
        index = 0

        while index *2 <= len(self.data) -1:
            minIndex = self.__getMinIndex(index)
            if self.data[minIndex] > self.data[index]:
                self.data[minIndex], self.data[index] = self.data[index], self.data[minIndex]
                index = minIndex
            else:
                break

    def __getMinIndex(self,i):
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
print q.extractMax()
