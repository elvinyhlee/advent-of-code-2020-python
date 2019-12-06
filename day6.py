#1
obj = {}
with open('day6-data.txt') as f:
    for ix, line in enumerate(f):
        data = [str(x.strip()) for x in line.split(')')]
        a = data[0]
        b = data[1]
        if a in obj:
            obj[a].append(b)
        else:
            obj[a] = [b]

    num = 0
    q = ['COM']
    count = 0
    while q:
        l = len(q)
        for i in range(l):
            count += num
            if q[i] in obj:
                for j in obj[q[i]]:
                    q.append(j)

        for i in range(l):
            q.pop(0)

        num += 1
        
    print(count)
    
f.close()


#2
obj = {}
with open('day6-data.txt') as f:
    for ix, line in enumerate(f):
        data = [str(x.strip()) for x in line.split(')')]
        a = data[0]
        b = data[1]
        if a in obj:
            obj[a].append(b)
        else:
            obj[a] = [b]

    def find_way(position, target, path):
        p = path + [position]

        if position == target:
            return p
        else:
            if position in obj:
                for i in obj[position]:
                    w = find_way(i, target, p)
                    if w:
                        return w
    
    check = False
    position = 'COM'
    you_target = 'YOU'
    santa_target = 'SAN'
    you_path = find_way(position, you_target, [])
    santa_path = find_way(position, santa_target, [])

    you_index = 0
    santa_index = 0
    for ix, i in enumerate(you_path):
        for jx, j in enumerate(santa_path):
            if j == i:
                you_index = ix + 2
                santa_index = jx + 2
    ans = (len(you_path) - you_index) + (len(santa_path) - santa_index)
    print(ans)

f.close()