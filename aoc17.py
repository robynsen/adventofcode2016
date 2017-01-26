import sys
import hashlib
import time

def isUnlocked(my_input, my_path, my_dir):
    # my_dir is one of 'U', 'D', 'L', 'R'
    result = False
    my_dirs = {'U':0, 'D':1, 'L':2, 'R':3}
    result = (hashlib.md5(('%s%s' % (my_input, my_path)).encode('utf-8')).hexdigest()[my_dirs[my_dir]] in ('b', 'c', 'd', 'e','f'))
    return result

def isDoor(x, y, my_dir):
    dx = get_dx(my_dir)
    dy = get_dy(my_dir)
    
    result = (((x + dx) >=0) and ((y + dy) >=0) and ((x + dx) < 4) and ((y + dy) < 4))
    return result

def get_dx(my_dir):
    dx = {'U':0, 'D':0, 'L':-1, 'R':1}
    return dx[my_dir]

def get_dy(my_dir):
    dy = {'U':-1, 'D':1, 'L':0, 'R':0}
    return dy[my_dir]

def is_same_pos(a, b):
    return ((a[0] == b[0]) and (a[1] == b[1]))

def getNextSteps(my_input, myPos):
    myNextSteps = []
    x = myPos[0]
    y = myPos[1]
    my_path = myPos[2]

    for next_dir in ('U', 'D', 'L', 'R'):
        if (isDoor(x, y, next_dir) and isUnlocked (my_input, my_path, next_dir)):

            myNextSteps.append((x + get_dx(next_dir), y + get_dy(next_dir), "%s%s" % (my_path, next_dir)))

    return myNextSteps

def bfs_part1(my_input):
    PATH_INDEX = 2
    start = (0, 0, '')
    end = (3, 3, '')
    # parentRef = {}
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)

        if is_same_pos(node, end):
            return node[PATH_INDEX]

        for child in getNextSteps(my_input, node):
            queue.append(child)


def bfs_part2(my_input):
    PATH_INDEX = 2

    start = (0, 0, '')
    end = (3, 3, '')
    len_longest_path = 0
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)

        if is_same_pos(node, end):
            if len(node[PATH_INDEX]) > len_longest_path:
                len_longest_path = len(node[PATH_INDEX])
        else:
            for child in getNextSteps(my_input, node):
                queue.append(child)
    return len_longest_path

if __name__ == '__main__':
    my_start = time.monotonic()

    if len(sys.argv[1:]) == 0:
        print('Usage: aoc17.py [--part1 | --part2]')
        quit()

    part_no = 1    
    if '--part2' in sys.argv[1:]:
        part_no = 2    
    
    for my_str in ('ihgpwlah', 'kglvqrro', 'ulqzkmiv', 'njfxhljp'):
        if (part_no == 1):
            print (' ', my_str, '-->', bfs_part1(my_str))
        else:
            print (' ', my_str, '-->', bfs_part2(my_str))

    print ('------------------')
    print (" Elapsed time: %.5f s" % (time.monotonic() - my_start))
