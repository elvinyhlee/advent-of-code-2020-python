#1
with open('day10-data.txt') as f:
    from math import sqrt
    data = []
    ans = 0
    for ix, line in enumerate(f):
        data += [(jx, ix) for jx, i in enumerate(line) if i == '#']
    
    def distance(a,b):
        return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def is_between(a,b,c):
        return abs(distance(a,c) + distance(c,b) - distance(a,b)) < 0.00000000001
    
    for i in data:
        count = 0
        for j in data:
            if i != j:
                check = True
                for k in data:
                    if (k == i) or (k == j): 
                        pass
                    elif is_between(i, j, k):
                        check = False
                        
                if check:
                    count += 1
        if count > ans:
            print(i)
        ans = max(ans, count)

    print(ans)
f.close()

#2

with open('day10-data.txt') as f:
    from math import sqrt, pi
    import numpy as np
    data = []
    # last_ans = (37,25)
    last_ans = (11,13)
    
    for ix, line in enumerate(f):
        data += [(jx, ix) for jx, i in enumerate(line) if i == '#']
    
    def distance(a,b):
        return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def is_between(a,b,c):
        return abs(distance(a,c) + distance(c,b) - distance(a,b)) < 0.00000000001
    
    def angle_between(p1, p2):
        ang1 = np.arctan2(*p1[::-1])
        ang2 = np.arctan2(*p2[::-1])
        return np.rad2deg((ang1 - ang2) % (2 * np.pi))

    ans = []

    for j in data:
        if last_ans != j:
            check = True
            for k in data:
                if (k == last_ans) or (k == j): 
                    pass
                elif is_between(last_ans, j, k):
                    check = False
                    
            if check:
                x, y = j
                angle = np.arctan2(x-11, y-13)
                ans += [(j, (angle if angle > 0 else (2*pi + angle) * 360 / (2*pi)))]
    
    ans = sorted(ans, key=lambda x: x[1])
    print(ans[199])
f.close()