from Node import *
"import pudb; pu.db"

t = Node(5)
for i in range(1,10):
    t.insert(i)

t.printTree()
print "count = ", t.count()
print "Does 6 exist: ", t.search(6)
