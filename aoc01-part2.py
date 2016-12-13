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
            if [i, y] in visitedsites and found == 0:
                found = 1
                print(abs(i) + abs(y))
            visitedsites.append([i,y])
        else:
            if [x, i] in visitedsites and found == 0:
                found = 1
                print(abs(x) + abs(i))
            visitedsites.append([x,i])
    prev_x = x
    prev_y = y