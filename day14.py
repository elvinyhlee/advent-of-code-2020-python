import re
import itertools


class Decoder:
    def __init__(self, mask_string=None):
        self.mask_0 = 2 ** 36 - 1
        self.mask_1 = 0
        self.mask_x_positions = []
        if mask_string:
            for ix, mask in enumerate(reversed(mask_string)):
                if mask == '0':
                    self.mask_0 -= 2 ** ix
                elif mask == '1':
                    self.mask_1 += 2 ** ix
                elif mask == 'X':
                    self.mask_x_positions.append(ix)

    def decode(self, value: int, overwrite_with_0: bool, overwrite_with_1: bool, x_is_float: bool) -> int or list[int]:
        decoded_value = value

        if overwrite_with_0:
            decoded_value &= self.mask_0

        if overwrite_with_1:
            decoded_value |= self.mask_1

        if x_is_float:
            # Set all positions of X to 0
            decoded_value &= (2 ** 36 - 1) - sum(2 ** ix for ix in self.mask_x_positions)

            # Return all combinations
            return [
                decoded_value + sum(2 ** self.mask_x_positions[ix] for ix, value in enumerate(values) if value == 1)
                for values in itertools.product([0, 1], repeat=len(self.mask_x_positions))
            ]
        else:
            return [decoded_value]


def extract_mask(data: str) -> str:
    return data.split(' ')[-1]


def extract_address_and_value(data: str) -> (int, int):
    address = int(re.search(r'\[(.*?)\]', data).group(1))
    value = int(data.split(' ')[-1])
    return address, value


def run(lines, part):
    memory = {}
    decoder = Decoder()

    for line in lines:
        if 'mask' in line:
            mask_string = extract_mask(line)
            decoder = Decoder(mask_string)
        else:
            address, value = extract_address_and_value(line)

            if part == 1:
                memory[address] = decoder.decode(value, True, True, False)[0]

            elif part == 2:
                addresses = decoder.decode(address, False, True, True)
                for ad in addresses:
                    memory[ad] = value

    return sum(memory.values())


with open('day14-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(run(inputs, part=1))
    print(run(inputs, part=2))
