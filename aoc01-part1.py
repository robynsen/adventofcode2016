file = open('aoc01-input.txt', 'r')
moves = file.readline().strip().split(", ")
# north = 0, east = 1, south = 2, west = 3
orientation = 0
x = 0
y = 0
for m in moves:
    if m[0] == 'L':
        orientation -= 1
    else:
        orientation += 1
    orientation %= 4

    d = int(m[1:])
    if orientation == 0:
        y += d
    elif orientation == 1:
        x += d
    elif orientation == 2:
        y -= d
    elif orientation == 3:
        x -= d
print(abs(x) + abs(y))