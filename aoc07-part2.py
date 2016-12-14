import re
import collections

# returns all x,y pairs where xyx is in my_str
def get_abbas(my_str, check_type):
    result = []
    if len(my_str) >= 3:
        for i in range(0,len(my_str)-2):
            if (my_str[i] == my_str[i+2] and my_str[i] != my_str[i+1]):
                if check_type == 'INNER':
                    result.append([my_str[i],my_str[i+1]])
                elif check_type == 'OUTER':
                    result.append([my_str[i+1],my_str[i]])
    return result

with open('aoc07-input.txt', 'r') as infile:
    regex = re.compile(r"([a-z]+[\[\]\n])")
    ssl_sum = 0
    for line in infile:
        result = regex.findall(line)
        inner_abas = []
        outer_abas = []
        ssl_string = False

        for r in result:
            if r[-1] == ']':
                inner_abas += get_abbas(r, 'INNER')
            else:
                outer_abas += get_abbas(r, 'OUTER')
        for c in inner_abas:
            if c in outer_abas:
                ssl_string = True
        if ssl_string:
            ssl_sum += 1
    print(ssl_sum)