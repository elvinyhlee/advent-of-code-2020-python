#1

with open('day8-data.txt') as f:
    line = f.readline()
    ix = 0
    max_0 = 2147483641
    wide = 25
    tall = 6
    ans = 0

    while ix < len(line):
        if ix % (wide*tall) == 0:
            num_0 = 0
            num_1 = 0
            num_2 = 0
        if line[ix] == '0':
            num_0 += 1
        elif line[ix] == '1':
            num_1 += 1
        elif line[ix] == '2':
            num_2 += 1

        if (ix % (wide*tall) == (wide*tall -1)) and num_0 < max_0:
            max_0 = num_0
            ans = num_1 * num_2

        ix += 1
        
    print(ans)

f.close()

#2

with open('day8-data.txt') as f:
    line = f.readline()
    ix = 0
    wide = 25
    tall = 6
    final = ['2' for i in range(wide*tall)]

    while ix < len(line):
        m = ix % (wide*tall)
        if line[ix] == '0' and final[m] == '2':
            final[m] = '0'
        elif line[ix] == '1' and final[m] == '2':
            final[m] = '1'
        ix += 1

    ix = 0
    for i in range(tall):
        k = ''
        for j in range(wide):
            k += final[ix]
            ix += 1
        print(k)

f.close()