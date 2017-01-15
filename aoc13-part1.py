
def isSpace(x, y):
    return (bin(x*x + 3*x + 2*x*y + y + y*y + 1364).count("1") % 2 == 0)

def getNextSteps(myPos):
    myNextSteps = []
    x = myPos[0]
    y = myPos[1]

    if (x - 1 >= 0) and isSpace(x-1, y):
        myNextSteps.append((x-1, y))
    if isSpace(x+1, y):
        myNextSteps.append((x+1, y))
    if (y - 1 >= 0) and isSpace(x, y-1):
        myNextSteps.append((x, y-1))
    if isSpace(x, y+1):
        myNextSteps.append((x,y+1))
    return myNextSteps

def bfs():
    start = (1, 1)
    end = (31, 39)
    parentRef = {}
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)

        if node == end:
            return backtrace(parentRef, start, end)

        for child in getNextSteps(node):
            if child not in parentRef:
                parentRef[child] = node
                queue.append(child)

def backtrace(parent, start, end):
    i = 0
    tmp = end
    while tmp != start:
        tmp = parent[tmp]
        i += 1
    return i

if __name__ == '__main__':
    print ('Distance is', bfs())
