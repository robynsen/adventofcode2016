with open('aoc03-input.txt') as fp:
    i = 0
    for line in fp:
        sides = [int(n) for n in line.split()]
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            i += 1
    print(i)