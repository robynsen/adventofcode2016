import collections

with open('aoc06-input.txt', 'r') as infile:
    input_rows = []
    input_cols = []
    message = list("")

    for line in infile:
        input_rows.append(list(line.strip()))
    input_cols = zip(*input_rows)
    
    for col in input_cols:
        message.append(collections.Counter(col).most_common(1)[0][0])
    print(''.join(message))