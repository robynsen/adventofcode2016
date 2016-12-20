with open('aoc02-input.txt') as fp:
    pos = 5
    for line in fp:
        moves = list(line.strip())
        for m in moves:
            if m == 'U':
                if pos in [3, 13]:
                    pos -= 2
                elif pos in [6,7,8,10,11,12]:
                    pos -= 4
            elif m == 'D':
                if pos in [1, 11]:
                    pos += 2
                elif pos in [2,3,4,6,7,8]:
                    pos += 4
            elif m == 'L' and pos in [3,4,6,7,8,9,11,12]:
                pos -= 1
            elif m == 'R' and pos in [2,3,5,6,7,8,10,11]:
                pos += 1
        print(format(pos,'1X'), end="")
