#1
position_1 = set()
position_2 = set()
ans = 2147483647
with open('day3-data.txt') as f:
    for ix, line in enumerate(f):
        data = [l.strip() for l in line.split(',')]
        x = 0
        y = 0
        for d in data:
            num = int(d[1:])
            x_delta = 0
            y_delta = 0
            if d[0] == 'R':
                x_delta = 1
            elif d[0] == 'L':
                x_delta = -1
            elif d[0] == 'U':
                y_delta = 1
            elif d[0] == 'D':
                y_delta = -1

            for i in range(num):
                x = x + x_delta
                y = y + y_delta
                if ix == 0:
                    position_1.add((x, y))
                elif ix == 1:
                    position_2.add((x, y))

    intersections = position_1.intersection(position_2)
    
    for i, j in intersections:
        ans = min(ans, abs(i) + abs(j))

print(ans)
f.close()

#2
position_1 = set()
position_2 = set()
position_1_with_count = set()
position_2_with_count = set()
ans = 2147483647
with open('day3-data.txt') as f:
    for ix, line in enumerate(f):
        data = [l.strip() for l in line.split(',')]
        x = 0
        y = 0
        count = 0
        for d in data:
            num = int(d[1:])
            x_delta = 0
            y_delta = 0
            if d[0] == 'R':
                x_delta = 1
            elif d[0] == 'L':
                x_delta = -1
            elif d[0] == 'U':
                y_delta = 1
            elif d[0] == 'D':
                y_delta = -1

            for i in range(num):
                count += 1
                x = x + x_delta
                y = y + y_delta
                if ix == 0:
                    position_1.add((x, y))
                    position_1_with_count.add(((x, y),count))
                elif ix == 1:
                    position_2.add((x, y))
                    position_2_with_count.add(((x, y),count))

    intersections = position_1.intersection(position_2)
    
    for i in intersections:
        k = 0
        for j in position_1_with_count:
            if j[0] == i:
                k += j[1]
                break
        for j in position_2_with_count:
            if j[0] == i:
                k += j[1]
                break
        ans = min(ans, k)

print(ans)
f.close()
