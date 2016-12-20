import re
import collections

with open('aoc09-input.txt', 'r') as infile:
    regex = re.compile(r"\(([0-9]+)x([0-9]+)\)")
    for line in infile:
        my_str = line.strip()
        my_weights = [1] * len(my_str)

        for i in range(len(my_str)):
            # e.g. input A  (  1  x  5  )  B  C
            #      value       n     m
            #      index    i              j  j+n
            #     weight 1  0  0  0  0  0  5  1
            if my_str[i] == '(':
                re_result = regex.search(my_str[i:])
                n = re_result.group(1)
                m = re_result.group(2)
                j = i + 3 + len(n) + len(m)

                k = i
                while k < j:
                    my_weights[k] = 0
                    k += 1

                k = j
                while k < j + int(n):
                    my_weights[k] *= int(m)
                    k += 1
                i = j
            else:
                i += 1
    print(sum(my_weights))