import sys
import time
import re

if __name__ == '__main__':
    my_start = time.monotonic()
    LOWER_BOUND = 0
    UPPER_BOUND = 1

    part_no = 1
    my_filename = 'aoc20-input.txt'

    if '--part2' in sys.argv[1:]:
        part_no = 2
    
    if '--test' in sys.argv[1:]:
        my_filename = 'aoc20-testinput.txt'

    with open(my_filename, 'r') as infile:
        my_firewall = []
        regex = re.compile("([0-9]+)-([0-9]+)")
        for line in infile:
            result = regex.search(line)
            my_x = int(result.group(1))
            my_y = int(result.group(2))

            my_firewall.append((int(result.group(1)), int(result.group(2))))

        my_firewall.sort(key=lambda x: x[LOWER_BOUND])

        print ('------------------')
    
        min_ip = 0
        num_ips = 0
        max_checked = 0

        if my_firewall[0][LOWER_BOUND] == min_ip:
            for i in range (len(my_firewall) - 1):
                max_checked = max(max_checked, my_firewall[i][UPPER_BOUND])
                if max_checked + 1 < my_firewall[i+1][LOWER_BOUND]:                    
                    if min_ip == 0:
                        min_ip = max_checked + 1
                    num_ips += (my_firewall[i+1][LOWER_BOUND] - (max_checked + 1))
        print ('Part 1: smallest IP =\t', min_ip)
        print ('Part 2: number of IPs =\t', num_ips)

    print ('------------------')
    print (" Elapsed time: %.5f s" % (time.monotonic() - my_start))