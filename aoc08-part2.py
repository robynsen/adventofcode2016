import re
import collections

def switch_on(my_matrix, a,b):
    for i in range (0,a):
        for j in range (0,b):
            my_matrix[j][i] = 1
    return my_matrix

def rotate_row(my_matrix, index, diff):
    r = ''.join(str(x) for x in my_matrix[index])
    n = (len(r) - diff) % len(r)
    r = "%s%s" % (r[n:], r[:n])
    my_matrix[index] = list(map(int, r))
    return my_matrix

# rotate_col(A) == Transpose(rotate_row(Transpose(A)))
def rotate_col(my_matrix, index, diff):
    t_matrix = list(map(list, zip(*my_matrix)))
    r_matrix = rotate_row(t_matrix, index, diff)
    my_matrix = list(map(list, zip(*r_matrix)))
    return my_matrix

def print_parts(my_matrix):
    for i in range(10):
        for j in range(6):
            print(''.join(map(str, my_matrix[j][i*5:(i+1)*5])))
        print ('-----')

with open('aoc08-input.txt', 'r') as infile:
    w, h = 50, 6
    my_matrix = [[0 for x in range(w)] for y in range(h)] 

    re_rect = re.compile(r"rect\s([0-9]+)x([0-9]+)")
    re_row = re.compile(r"rotate\srow\sy\=([0-9]+)\sby\s([0-9]+)")
    re_col = re.compile(r"rotate\scolumn\sx\=([0-9]+)\sby\s([0-9]+)")
    for line in infile:
        if line[:4] == 'rect':
            re_result = re_rect.search(line)
            x = int(re_result.group(1))
            y = int(re_result.group(2))
            my_matrix = switch_on(my_matrix, x, y)
        elif line[:10] == 'rotate row':
            re_result = re_row.search(line)
            index = int(re_result.group(1))
            diff = int(re_result.group(2))
            my_matrix = rotate_row(my_matrix, index, diff)
        elif line[:13] == 'rotate column':
            re_result = re_col.search(line)
            index = int(re_result.group(1))
            diff = int(re_result.group(2))
            my_matrix = rotate_col(my_matrix, index, diff)
    print_parts(my_matrix)