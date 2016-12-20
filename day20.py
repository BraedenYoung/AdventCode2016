
from termcolor import cprint


SAMPLES = """
    5-8
    22-23
    0-2
    4-7
    3-15
    32-33
"""


def part_one(input):
    cprint("Day 20: part one ", 'green')

    black_list = []

    for line in input.splitlines():
        if not line:
            continue
        lower, higher = map(int, line.split('-'))
        black_list.append((lower, higher))

    black_list = sorted(black_list, key=lambda x: x[0])

    print combine(black_list)[0][1] + 1


def combine(black_list):
    while True:
        combined = False
        for index, black in enumerate(black_list):
            if index == len(black_list) - 1:
                break
            if black[1]+1 >= black_list[index+1][0]:
                new_higher = max(black_list[index][1], black_list[index+1][1])
                black_list[index] = (black_list[index][0], new_higher)
                black_list.pop(index+1)
                combined = True

        if not combined:
            break
    return black_list


def part_two(input):
    cprint("Day 20: part two ", 'green')

    black_list = []

    for line in input.splitlines():
        if not line:
            continue
        lower, higher = map(int, line.split('-'))
        black_list.append((lower, higher))

    black_list = sorted(black_list, key=lambda x: x[0])
    black_list = combine(black_list)

    total = 0
    for index, black in enumerate(black_list):
        if index == len(black_list) - 1:
            break

        total += abs(black_list[index+1][0]-black[1])-1

    print total
