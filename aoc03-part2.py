from itertools import islice
with open('aoc03-input.txt', 'r') as infile:
    i = 0
    while True:
        lines = list(islice(infile, 3))
        if not lines:
            break

        line0 = [int(n) for n in lines[0].split()]
        line1 = [int(n) for n in lines[1].split()]
        line2 = [int(n) for n in lines[2].split()]

        t0 = [line0[0], line1[0], line2[0]]
        t1 = [line0[1], line1[1], line2[1]]
        t2 = [line0[2], line1[2], line2[2]]

        for t in [t0, t1, t2]:
            t.sort()
            if t[0] + t[1] > t[2]:
                i += 1
    print(i)