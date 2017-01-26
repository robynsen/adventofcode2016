import time
import sys

def dragonify(my_bits):
    debug = True
    # reverse bits
    tmp = reverse_bits(my_bits)
    
    # flip bits manually instead of tmp = ~tmp 
    my_mask = 0
    for i in range(my_input_len):
        my_mask = my_mask << 1 | 1
    tmp = tmp ^ my_mask

    return ((my_bits << my_input_len + 1) | tmp)

# based on: http://stackoverflow.com/a/5333602
def reverse_bits(x):
    result = 0
    # refer to my_input_len, rather than x.bit_length(), to preserve leading zeros
    num_bits = my_input_len
    for i in range(num_bits):                   # for each bit number
        if (x & (1 << i)):                        # if it matches that bit
            result |= (1 << (num_bits - 1 - i))   # set the "opposite" bit in answer
    return result

def get_checksum(my_str):
    while (len(my_str) % 2 == 0):
        my_tmp = ''
        for i in range(0, len(my_str) - 1, 2):
            my_char = '0'
            if (my_str[i] == my_str[i+1]):
                my_char = '1'
            my_tmp = ''.join((my_tmp, my_char))
        my_str = my_tmp
    return my_str

# housekeeping
if len(sys.argv[1:]) == 0:
    print('Usage: aoc16-part1.py [--part1 | --part2] [--test]')
    quit()

my_start = time.monotonic()

part_no = 1
my_input = '01111010110010011'
max_len = 272

if '--part2' in sys.argv[1:]:
    part_no = 2
    max_len = 35651584
    print ('Too inefficient, nope.')
    quit()

if '--test' in sys.argv[1:]:
    my_input = '10000'
    max_len = 20

# process input
my_bits = int(my_input, 2)
my_input_len = len(my_input)

print ('Input:', "{0:0{width}b}".format(my_bits, width=my_input_len))

while my_input_len < max_len:
    # specify the width to preserve leading zeros
    # print ("{0:0{width}b}".format(my_bits, width=my_input_len))
    my_bits = dragonify(my_bits)
    my_input_len = my_input_len*2 + 1

my_str = "{0:0{width}b}".format(my_bits, width=(my_input_len))[0:max_len]
print ('----------------------------')
print ('Checksum:', get_checksum(my_str))

print ('----------------------------')
print ("Elapsed time: %.5f s" % (time.monotonic() - my_start))