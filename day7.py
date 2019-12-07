#1
import copy
from itertools import permutations
def int_computer(data, input, phase):
    position = 0
    input_phase = False
    
    def get_position(mode, i):
        if mode == 0:
            return data[i]
        else:
            return i

    while position < len(data):
        num = data[position] % 100
        mode_1 = data[position] // 100 % 10
        mode_2 = data[position] // 1000 % 10
        mode_3 = data[position] // 10000 % 10
        if num == 1:
            data[get_position(mode_3, position+3)] = data[get_position(mode_1, position+1)] + data[get_position(mode_2, position+2)]
            position += 4
        elif num == 2:
            data[get_position(mode_3, position+3)] = data[get_position(mode_1, position+1)] * data[get_position(mode_2, position+2)]
            position += 4
        elif num == 3:
            if input_phase:
                data[get_position(mode_1, position+1)] = input
            else:
                data[get_position(mode_1, position+1)] = phase
                input_phase = True
            position += 2
        elif num == 4:
            return(data[get_position(mode_1, position+1)])
            position += 2
        elif num == 5:
            if data[get_position(mode_1, position+1)]:
                position = data[get_position(mode_2, position+2)]
            else:
                position += 3
        elif num == 6:
            if data[get_position(mode_1, position+1)] == 0:
                position = data[get_position(mode_2, position+2)]
            else:
                position += 3
        elif num == 7:
            if data[get_position(mode_1, position+1)] < data[get_position(mode_2, position+2)]:
                data[get_position(mode_3, position+3)] = 1
            else:
                data[get_position(mode_3, position+3)] = 0
            position += 4
        elif num == 8:
            if data[get_position(mode_1, position+1)] == data[get_position(mode_2, position+2)]:
                data[get_position(mode_3, position+3)] = 1
            else:
                data[get_position(mode_3, position+3)] = 0
            position += 4
        elif num == 99:
            break


with open('day7-data.txt') as f:
    line = f.readline()
    data = [int(x.strip()) for x in line.split(',')]
    phases = 5
    ans = 0
    for j in permutations(range(phases), 5):
        permutation = list(j)
        input_arg = 0
        for k in permutation:
            d = copy.deepcopy(data)
            input_arg = int_computer(d, input_arg, k)
        ans = max(ans, input_arg)
    print(ans)

f.close()


#2
import copy
from itertools import permutations
def int_computer(data, input, phase, input_phase, position=0):
    
    def get_position(mode, i):
        if mode == 0:
            return data[i]
        else:
            return i

    while position < len(data):
        num = data[position] % 100
        mode_1 = data[position] // 100 % 10
        mode_2 = data[position] // 1000 % 10
        mode_3 = data[position] // 10000 % 10
        if num == 1:
            data[get_position(mode_3, position+3)] = data[get_position(mode_1, position+1)] + data[get_position(mode_2, position+2)]
            position += 4
        elif num == 2:
            data[get_position(mode_3, position+3)] = data[get_position(mode_1, position+1)] * data[get_position(mode_2, position+2)]
            position += 4
        elif num == 3:
            if input_phase:
                data[get_position(mode_1, position+1)] = input
            else:
                data[get_position(mode_1, position+1)] = phase
                input_phase = True
            position += 2
        elif num == 4:
            return(data[get_position(mode_1, position+1)]), position+2
            position += 2
        elif num == 5:
            if data[get_position(mode_1, position+1)]:
                position = data[get_position(mode_2, position+2)]
            else:
                position += 3
        elif num == 6:
            if data[get_position(mode_1, position+1)] == 0:
                position = data[get_position(mode_2, position+2)]
            else:
                position += 3
        elif num == 7:
            if data[get_position(mode_1, position+1)] < data[get_position(mode_2, position+2)]:
                data[get_position(mode_3, position+3)] = 1
            else:
                data[get_position(mode_3, position+3)] = 0
            position += 4
        elif num == 8:
            if data[get_position(mode_1, position+1)] == data[get_position(mode_2, position+2)]:
                data[get_position(mode_3, position+3)] = 1
            else:
                data[get_position(mode_3, position+3)] = 0
            position += 4
        elif num == 99:
            return None, position


with open('day7-data.txt') as f:
    line = f.readline()
    data = [int(x.strip()) for x in line.split(',')]    
    ans = 0

    for j in permutations(range(5, 10), 5):
        permutation = list(j)
        input_arg = 0
        ix = 0
        init = False
        final_arg = None
        d0 = copy.deepcopy(data)
        d1 = copy.deepcopy(data)
        d2 = copy.deepcopy(data)
        d3 = copy.deepcopy(data)
        d4 = copy.deepcopy(data)
        p0, p1, p2, p3, p4 = 0, 0, 0, 0, 0
        while input_arg is not None:
            if ix == 0:
                d = d0
                input_arg, p0 = int_computer(d, input_arg, permutation[ix], init, p0)
            elif ix == 1:
                d = d1
                input_arg, p1 = int_computer(d, input_arg, permutation[ix], init, p1)
            elif ix == 2:
                d = d2
                input_arg, p2 = int_computer(d, input_arg, permutation[ix], init, p2)
            elif ix == 3:
                d = d3
                input_arg, p3 = int_computer(d, input_arg, permutation[ix], init, p3)
            elif ix == 4:
                d = d4
                input_arg, p4 = int_computer(d, input_arg, permutation[ix], init, p4)
    
            if ix == 4 and input_arg:
                final_arg = input_arg
            if ix == 4:
                init = True
    
            ix = (ix + 1) % 5
    
        if final_arg:
            ans = max(ans, final_arg)
        
    print(ans)

f.close()