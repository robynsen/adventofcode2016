import re
import collections

with open('aoc09-input.txt', 'r') as infile:
    regex = re.compile(r"\(([0-9]+)x([0-9]+)\)")
    sector_sum = 0
    for line in infile:
        new_list = []
        i = 0
        while i < len(line):
            if line[i] == '(':
                re_result = regex.search(line[i:])
                m = re_result.group(1)
                n = re_result.group(2)
                i += 3 + len(n) + len(m)
                
                for j in range(int(m)):
                    for k in range(int(n)):
                        new_list.append(line[i])
                i += int(m)
            else:
                i += 1
        print(len(new_list))