import re
import time
import sys

def isPathClear(delta_t, disc_t0_pos, disc_mod_n):
    result = True
    for i in disc_t0_pos:
        delta_t += 1
        if ((disc_t0_pos[i] + delta_t) % disc_mod_n[i]) != 0:
            result = False
    return result

# housekeeping
if len(sys.argv[1:]) == 0:
    print('Usage: aoc14.py [--part1 | --part2]')
    quit()

my_start = time.monotonic()

part_no = 1
if '--part2' in sys.argv[1:]:
    part_no = 2

# process input
disc_t0_pos = {}
disc_mod_n = {}
with open('aoc15-part1-input.txt', 'r') as infile:
    # Disc #1 has 7 positions; at time=0, it is at position 0.
    regex = re.compile("Disc #([0-9]+) has ([0-9]+) positions; at time=([0-9]+), it is at position ([0-9]+)\.")
    for line in infile:
        result = regex.search(line)

        disc_num = int(result.group(1))
        mod_n = int(result.group(2))
        time_t = int(result.group(3))
        start_pos = int(result.group(4))

        # preemptively captured time_t because i assumed part2 would ask for this... -_-
        disc_t0_pos[disc_num - 1] = start_pos - time_t % mod_n
        disc_mod_n[disc_num - 1] = mod_n

if part_no == 2:
    # a new disc with 11 positions and starting at position 0 has appeared exactly one second below the previously-bottom disc.
    disc_t0_pos[len(disc_t0_pos)] = 0
    disc_mod_n[len(disc_mod_n)] = 11

# search for first successful opportunity to press button
start_t = 0
result_found = False
while (not result_found):
    result_found = isPathClear(start_t, disc_t0_pos, disc_mod_n)
    start_t += 1

print ('Press button when t=', start_t - 1)

print ("Elapsed time: %.2f s" % (time.monotonic() - my_start))