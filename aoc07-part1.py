import re
import collections

def has_abba(my_str):
    result = False
    if len(my_str) >= 4:
        for i in range(0,len(my_str)-3):
            if (my_str[i] == my_str[i+3] and my_str[i+1] == my_str[i+2] and my_str[i] != my_str[i+1]):
                result = True
    return result

with open('aoc07-input.txt', 'r') as infile:
    regex = re.compile(r"([a-z]+[\[\]\n])")
    support_sum = 0
    for line in infile:
        result = regex.findall(line)
        outer_ok = False
        inner_ok = True
        for r in result:
            if r[-1] == ']' and has_abba(r):
                inner_ok = False
            elif has_abba(r):
                outer_ok = True
        if (inner_ok and outer_ok):
            support_sum += 1
    print(support_sum)