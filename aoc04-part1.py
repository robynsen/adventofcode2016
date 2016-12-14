import re
import collections

with open('aoc04-input.txt', 'r') as infile:
    regex = re.compile("([a-z\-]+)-([0-9]+)\[([a-zA-Z]+)\]")
    sector_sum = 0
    for line in infile:
        result = regex.search(line)
        e_name = result.group(1)
        sector_id = int(result.group(2))
        check_sum = result.group(3)
        
        freqs = collections.Counter(e_name.replace('-', '')).most_common()
        freqs.sort(key=lambda x: (-x[1], x[0]))
        top5 = "%s%s%s%s%s" % (freqs[0][0], freqs[1][0], freqs[2][0], freqs[3][0], freqs[4][0])
        if top5 == check_sum:
            sector_sum += sector_id
    print (sector_sum)
