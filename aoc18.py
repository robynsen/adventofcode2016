import sys
import time

def get_tile(my_pos, prev_row):
    # add the buffer so we don't fall off the edges of the row string when checking the edges
    my_buffered_row = '%s%s%s' % ('.', prev_row, '.')
    my_buffered_pos = my_pos + 1

    result = '.'
    # upper left tile is a trap xor upper right tile is a trap
    if ((my_buffered_row[my_buffered_pos-1] == '^') is not (my_buffered_row[my_buffered_pos+1] == '^')):
        result = '^'

    return result

def get_board(my_input, my_num_rows):
    my_board = []
    my_board.append(my_input)

    my_row_len = len(my_input)

    for i in range(1, my_num_rows):
        new_row = ''
        prev_row = my_board[i-1]
        for j in range(my_row_len):
            new_row = '%s%s' % (new_row, get_tile(j, prev_row))
        my_board.append(new_row)

        prev_row = new_row

    return my_board

if __name__ == '__main__':
    my_start = time.monotonic()

    if len(sys.argv[1:]) == 0:
        print('Usage: aoc18.py [--part1 | --part2] [--test]')
        quit()

    my_input = '......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..'
    my_num_rows = 40
    if '--part2' in sys.argv[1:]:
        my_num_rows = 400000
    
    if '--test1' in sys.argv[1:]:
        my_input = '..^^.'
        my_num_rows = 3

    if '--test2' in sys.argv[1:]:
        my_input = '.^^.^.^^^^'
        my_num_rows = 10

    my_board = get_board(my_input, my_num_rows)
    num_safe_tiles = 0

    print ('------------------')
    print ('Input:\t', my_input)
    print ('------------------')
    for i in range(len(my_board)):
        # count number of traps in row
        num_safe_tiles += my_board[i].count('.')
        # print (i,'\t', my_board[i])

    print ('------------------')
    print ('Safe tiles:\t', num_safe_tiles)
    print ('------------------')
    print (" Elapsed time: %.5f s" % (time.monotonic() - my_start))