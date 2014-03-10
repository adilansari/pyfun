def find(case, credit, list):
    list.sort()
    print list
    start, end = 0, len(list)-1
    while start < end:
        if (list[start]+list[end]) == credit:
            print 'Case #{0}: {1} {2}'.format(case, start, end)
            break
        elif (list[start] + list[end]) < credit:
            start+=1
        else:
            end-=1

file = open("inputs/A-small-practice.in","r")
tests = int(file.readline())

for n in range(1,tests+1):
    credit = int(file.readline())
    items =int(file.readline())
    list = [int(i) for i in file.readline().split()]
    print "Credit:{0}".format(credit)
    print "Items:{0}".format(items)
    find(n, items, list)
