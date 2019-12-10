#1

def int_computer(data, input, position, relative_base):
    
    def get_position(mode, i):
        p = 0
        if mode == 0:
            p = data[i]
        elif mode == 1:
            p = i
        elif mode == 2:
            if relative_base + i > len(data):
                for k in range(relative_base + i - len(data) + 1):
                    data.append(0)
            p = data[relative_base + i]

        if p > len(data):
            for k in range(p - len(data) + 1):
                data.append(0)

        return p

    while True:
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
            data[get_position(mode_1, position+1)] = input
            position += 2
        elif num == 4:
            print(data[get_position(mode_1, position+1)])
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
        elif num == 9:
            relative_base += data[get_position(mode_1, position+1)]
            position += 2
        elif num == 99:
            break


with open('day9-data.txt') as f:
    line = f.readline()
    data = [int(x.strip()) for x in line.split(',')]
    relative_base = 0
    position = 0
    single_input = 1
    
    int_computer(data, single_input, position, relative_base)

f.close()