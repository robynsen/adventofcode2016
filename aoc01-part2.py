file = open('aoc01-input.txt', 'r')
moves = file.readline().strip().split(", ")
# north = 0, east = 1, south = 2, west = 3
orientation = 0
x = 0
y = 0
prev_x = 0
prev_y = 0
visitedsites = []
found = 0

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

    if x < prev_x:
        my_range = range(x, prev_x)
    elif x > prev_x:
        my_range = range(x, prev_x, -1)
    elif y < prev_y:
        my_range = range(y, prev_y)
    elif y > prev_y:
        my_range = range(y, prev_y, -1)

    for i in my_range:
        if y == prev_y:
            a, b = i, y
        else:
            a, b = x, i
        if [a, b] in visitedsites and found == 0:
            found = 1
            print(abs(a) + abs(b))
        visitedsites.append([a,b])
    prev_x, prev_y = x, y