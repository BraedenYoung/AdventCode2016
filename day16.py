
from termcolor import cprint


FILL_LENGTH = 272


def part_one(input):
    cprint("Day 16: part one ", 'green')

    for line in input.splitlines():
        if not line:
            continue
        data = line

    while True:
        if len(data) >= FILL_LENGTH:
            break
        data = dragon_curve(data)

    print generate_checksum(data[:FILL_LENGTH])


def dragon_curve(data):

    a = data
    b = ''.join('1' if digit == '0' else '0' for digit in a[::-1])
    return a + '0' + b


def generate_checksum(data):

    checksum = data
    while True:
        possible_checksum = ''
        for pair in pair_generator(checksum):
            if pair in ('11', '00'):
                possible_checksum += '1'
            else:
                possible_checksum += '0'

        checksum = possible_checksum

        if len(checksum) % 2 != 0:
            break

    return checksum


def pair_generator(data):
    for pos in range(0, len(data), 2):
        yield data[pos:pos+2]


def part_two(input):
    cprint("Day 16: part two ", 'green')

    global FILL_LENGTH
    FILL_LENGTH = 35651584

    part_one(input)
