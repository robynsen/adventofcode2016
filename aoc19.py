import sys
import time

def find_winner_part1(my_input):
    # initialise list of indexes
    my_list = list(range(my_input))

    while (len(my_list) > 2):
        odd_row = False
        if (len(my_list) % 2 != 0):
            odd_row = True
        # remove every even index
        my_list = my_list[::2]

        if odd_row:
            # remove first item from list
            my_list.pop(0)
    return (my_list[0]+1)

def find_winner_part2(my_input):
    # range is 1..n+1 since elf position numbering begins at one
    my_list = list(range(1,my_input+1))

    # on the first loop, delete elves in the second half of the queue
    # on following repeat loops, delete elves from the full width of the queue until one remains
    # the pattern after all elves have taken one turn, is that the first two out of every three elves (ABC) loses their presents
    # my_skip tracks which one of the three positions (ABC) applies to position i

    i = int(my_input / 2) # we depend on this rounding down
    my_skip = 0
    if (my_input % 2 != 0):
        my_skip = 1

    while (len(my_list) > 1):
        next_skip = update_skip(my_list, i, my_skip) # calculate this before changing the list
        my_list = delete_elves(my_list, i, my_skip)
        my_skip = next_skip
        i = 0 
            
    return (my_list[0])

# my_list - list of elves' original indices
# start_i - the point in the list to begin deleting from
# my_skip - counter used to preserve every third elf in list
def delete_elves(my_list, start_i, my_skip):
    i = start_i

    # the offset values are similar to my_skip - they determine which of the three positions ABC is preserved
    my_offset_0 = 0
    my_offset_1 = 0
    if my_skip == 1:
        my_offset_0 = 0
        my_offset_1 = 1
    elif my_skip == 2:
        my_offset_0 = 1
        my_offset_1 = 1

    del my_list[start_i + my_offset_0::3]
    del my_list[start_i + my_offset_1::2]

    return my_list

# calculate the final skip number that delete_elves will land on given the same arguments
def update_skip(my_list, start_i, my_skip):
    return ((my_skip + len(my_list) - start_i) % 3)

if __name__ == '__main__':
    my_start = time.monotonic()

    if len(sys.argv[1:]) == 0:
        print('Usage: aoc19.py [--part1 | --part2] [--test]')
        quit()

    my_input = 3004953
    part_no = 1

    if '--part2' in sys.argv[1:]:
        part_no = 2
    
    if '--test' in sys.argv[1:]:
        my_input = 5

    print ('------------------')
    print ('Input:\t', my_input)
    print ('------------------')

    if part_no == 1:
        print ('Winner:\t', find_winner_part1(my_input))
    else:
        print ('Winner:\t', find_winner_part2(my_input))



    print ('------------------')
    print (" Elapsed time: %.5f s" % (time.monotonic() - my_start))