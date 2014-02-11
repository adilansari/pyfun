class Node(object):
    """Node of a binary tree"""

    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

    def insert(self , data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def search(self,data):

        if self.data == data:
            return True
        l, r = False, False
        
        if not self.left is None:
            l = self.left.search(data)
        if not self.right is None:
            r = self.right.search(data)

        return l or r

    def count(self):
        l , r =0,0
        if not self.left is None:
            l = self.left.count()
        if not self.right is None:
            r= self.right.count()

        return l + r +1

    def printTree(self):
        if self is None:
            return
        q = [self]
        current =1
        nxt = 0

        while not len(q) == 0:
            temp = q.pop(0)
            current -=1 
            if not temp.left is None:
                q.append(temp.left)
                nxt += 1
            if not temp.right is None:
                q.append(temp.right)
                nxt += 1

            print temp.data ,

            if current == 0:
                current, nxt = nxt,current
                print ""
