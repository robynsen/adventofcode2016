with open('aoc02-input.txt') as fp:
    pos = 5
    for line in fp:
        moves = list(line.strip())
        for m in moves:
            if m == 'U' and pos > 3:
                pos -= 3
            elif m == 'D' and pos < 7:
                pos += 3
            elif m == 'L' and pos not in [1,4,7]:
                pos -= 1
            elif m == 'R' and (pos % 3 != 0):
                pos += 1
        print(pos, end="")
