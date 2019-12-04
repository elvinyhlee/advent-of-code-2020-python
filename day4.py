#1
a = 134792
b = 675810

count = 0
for i in range(b-a):
    c = str(a + i)
    check = True
    check2 = False
    for ix, j in enumerate(c):
        if ix > 0 and (int(c[ix]) < int(c[ix-1])):
            check = False
        if ix > 0 and (c[ix] == c[ix-1]):
            check2 = True
    if check and check2:
        count += 1

print(count)        

#2
a = 134792
b = 675810

count = 0
g = []
for i in range(b-a):
    c = str(a + i)
    g = []
    check = True
    check2 = False
    check3 = False
    for ix, j in enumerate(c):
        g.append(0)

    for ix, j in enumerate(c):
        if ix > 0 and (int(c[ix]) < int(c[ix-1])):
            check = False
        if ix > 0 and (c[ix] == c[ix-1]):
            check2 = True
            g[ix] = g[ix-1] + 1

    for ix, j in enumerate(g):
        if (j == 1) and (ix == len(g)-1 or g[ix + 1] <= 1):
            check3 = True

    if check and check2 and check3:
        count += 1

print(count)