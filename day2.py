#1
with open('day2-data.txt') as f:
    line = f.readline()
    data = [int(x.strip()) for x in line.split(',')]
    data[1] = 12
    data[2] = 2
    for ix, num in enumerate(data):
        if ix % 4 == 0:
            if num == 1:
                data[data[ix+3]] = data[data[ix+1]] + data[data[ix+2]]
            elif num == 2:
                data[data[ix+3]] = data[data[ix+1]] * data[data[ix+2]]
            elif num == 99:
                break
                
    print(data[0])

f.close()

#2
import copy
with open('day2-data.txt') as f:
    line = f.readline()
    data = [int(x.strip()) for x in line.split(',')]
    expected_output = 19690720
    for noun in range(100):
        for verb in range(100):
            d = copy.deepcopy(data)
            d[1] = noun
            d[2] = verb
            for ix, num in enumerate(d):
                if ix % 4 == 0:
                    if num == 1:
                        d[d[ix+3]] = d[d[ix+1]] + d[d[ix+2]]
                    elif num == 2:
                        d[d[ix+3]] = d[d[ix+1]] * d[d[ix+2]]
                    elif num == 99:
                        break
            if d[0] == expected_output:
                print(100 * noun + verb)

f.close()