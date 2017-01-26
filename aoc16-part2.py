import time
import sys
from functools import reduce

def dragon_init(my_bits):
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
    result = ''

    my_len = len(my_str)
    my_digits = list(map(int, list(my_str)))
    # my_len = n * m where n is the largest odd divisor
    # each of the chunks of length m can be solved simply
    my_n = 1

    for i in range(my_len - 1, 0, -1):
        if my_len % i == 0 and i % 2 != 0 and my_n == 1:
            my_n = i
            print ('----------------------------')
            print ('Found largest odd divisor: n =', i)
    my_m = int(my_len / my_n)
    my_half_m = int(my_m / 2)

    my_digit = 0
    # there are n-many chunks of length m to be solved individually
    for i in range(my_n):
        my_digit = (sum(my_digits[i*my_m:(i+1)*my_m]) + my_half_m + 1) % 2
        result = ''.join((result, str(my_digit)))
        print ('\tn =', i,' ... checksum output updated to:', result)

    return result

# housekeeping
if len(sys.argv[1:]) == 0:
    print('Usage: aoc16-part2.py [--part1 | --part2] [--test]')
    quit()

my_start = time.monotonic()

part_no = 1
my_input = '01111010110010011'
max_len = 272

if '--part2' in sys.argv[1:]:
    part_no = 2
    max_len = 35651584

if '--test' in sys.argv[1:]:
    my_input = '10000'
    max_len = 20

# process input
my_bits = int(my_input, 2)
my_input_len = len(my_input)

print ('Input:\t', "{0:0{width}b}".format(my_bits, width=my_input_len))

# a 0 b
my_bits = dragon_init(my_bits)
my_input_len = my_input_len*2 + 1

# print ('a 0 b =\t', "{0:0{width}b}".format(my_bits, width=my_input_len))

while my_input_len < max_len:
    # specify the width to preserve leading zeros
    # print ("{0:0{width}b}".format(my_bits, width=my_input_len))
    my_bits = (my_bits << my_input_len + 1 | my_bits) + (1 << (int(my_input_len / 2)))
    my_input_len = my_input_len*2 + 1

my_str = "{0:0{width}b}".format(my_bits, width=(my_input_len))[0:max_len]

my_str = get_checksum(my_str)
print ('----------------------------')
print ('Tada, checksum:\t', my_str)
print ('----------------------------')
print ("Elapsed time: %.5f s" % (time.monotonic() - my_start))