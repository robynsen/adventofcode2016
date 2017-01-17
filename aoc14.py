import hashlib
import re
import time
import sys

# version now storing hashes for greater efficiency

def generateKey(part_no, my_str, i):
    h = hashlib.md5(('%s%s' % (my_str, str(i))).encode('utf-8')).hexdigest()
    if part_no == 2:
        for j in range(2016):
            h = hashlib.md5(('%s' % (h)).encode('utf-8')).hexdigest()
    return h

def updateHashes(part_no, my_str, i, my_hashes):
    if (i not in my_hashes):
        my_hashes[i] = generateKey(part_no, my_str, i)
    return my_hashes

if len(sys.argv[1:]) == 0:
    print('Usage: aoc14.py [--part2] [--testcase]')
    quit()

my_start = time.monotonic()

my_str = "qzyelonm"
part_no = 1

if '--testcase' in sys.argv[1:]:
    my_str = "abc"

if '--part2' in sys.argv[1:]:
    part_no = 2

i = 0
has_triple = {}
my_hashes = {}
my_keys = []

re_triple = re.compile(r'(\w)(\1{2,})')
re_quintuple = re.compile(r'(\w)(\1{4,})')

while len(my_keys) < 64:
    my_hashes = updateHashes(part_no, my_str, i, my_hashes)

    h = my_hashes[i]
    h_triple = re_triple.search(h)
    if h_triple is not None:
        # only consider the first triple in the string
        has_triple[i] = h_triple.group(0)[0]

        j = i+1
        # stop searching for quintuples once one is found for a given triple 
        quintuple_found = False
        while j < i+1001 and not quintuple_found:
            my_hashes = updateHashes(part_no, my_str, j, my_hashes)
            my_hash = my_hashes[j]
            my_quintuples = [match.group()[0] for match in re_quintuple.finditer(my_hash)]
            for k in my_quintuples:
                if has_triple[i] == k:
                    my_keys.append(i)
                    quintuple_found = True
                    print ('Key #',len(my_keys),'\t',my_hashes[i],'\tIndex:', i, 'Char:', k) 
                    print('   Quintuple\t', my_hash, '\tIndex:', j)
            j += 1
    i += 1
print ('\t\t-----------')
print ('Index of 64th key:', sorted(my_keys)[63])
print ('\t\t-----------')
print ('Index list:', sorted(my_keys))
print ('\t\t-----------')
print ("Elapsed time: %.2f s" % (time.monotonic() - my_start))