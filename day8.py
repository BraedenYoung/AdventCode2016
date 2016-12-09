
from termcolor import cprint

import numpy as np


SAMPLE = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
"""


def part_one(input):
    cprint("Day 8: part one ", 'green')

    light_array = np.zeros((6, 50), dtype=np.int)

    for line in input.splitlines():
        line = line.lstrip()
        input_digest = line.split(' ')

        if len(input_digest) == 2:
            handle_rect(light_array, input_digest[1])
            continue

        rotate_col = True if input_digest[1] == 'column' else False

        if rotate_col:
            handle_column_rotate(light_array, input_digest[2], input_digest[-1])
        else:
            handle_row_rotate(light_array, input_digest[2], input_digest[-1])

    print light_count(light_array)


def handle_rect(light_array, rect_size):
    col, row = map(int, rect_size.split('x'))
    for r in range(row):
        for c in range(col):
            light_array.itemset((r,c), 1)


def handle_column_rotate(light_array, column, amount):
    _, column = column.split('=')
    col_num = int(column)
    amount = int(amount)

    column = light_array[:, col_num]

    light_array[:, col_num] = np.roll(column, amount % len(column))


def handle_row_rotate(light_array, row, amount):
    _, row = row.split('=')
    row = int(row)
    amount = int(amount)

    light_array[row] = np.roll(light_array[row], amount)


def light_count(light_array):
    return np.sum(light_array)


SAMPLE_2 = 'xyxaba[xy]xyx[vababddd]'


def part_two(input):
    cprint("Day 8: part two ", 'green')

    light_array = np.zeros((6, 50), dtype=np.int)

    for line in input.splitlines():
        line = line.lstrip()
        input_digest = line.split(' ')

        if len(input_digest) == 2:
            handle_rect(light_array, input_digest[1])
            continue

        rotate_col = True if input_digest[1] == 'column' else False

        if rotate_col:
            handle_column_rotate(light_array, input_digest[2], input_digest[-1])
        else:
            handle_row_rotate(light_array, input_digest[2], input_digest[-1])

    for r in light_array:
        for c in r:
            print ('#' if c == 1 else ' '),
        print ''
