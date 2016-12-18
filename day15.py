from termcolor import cprint


SAMPLE = """
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
"""


def part_one(input):
    cprint("Day 15: part one ", 'green')

    cogs = {}

    positions = [0, ]

    for line in input.splitlines():
        if not line:
            continue
        line_decomp = line.split(' ')

        cog_num = int(line_decomp[1][1:])
        cogs[cog_num] = {
            'curr': int(line_decomp[11][:-1]),
            'total': int(line_decomp[3])
        }
        positions.append(cog_num)

    time_released = 0
    curr_time = 0

    while True:
        curr_time += 1

        if curr_time == len(positions):
            break

        if positions[curr_time] != 0:
            cog_num = positions[curr_time]
            if not check_for_collision(cogs, cog_num,
                                       time_released + curr_time):
                curr_time = 0
                time_released += 1

    print time_released


def check_for_collision(cogs, cog_num, time_past):

    if (time_past + cogs[cog_num]['curr']) % cogs[cog_num]['total'] != 0:
        return False

    return True


def part_two(input):
    cprint("Day 14: part two ", 'green')

    cogs = {}

    positions = [0,]

    for line in input.splitlines():
        if not line:
            continue
        line_decomp = line.split(' ')

        cog_num = int(line_decomp[1][1:])
        cogs[cog_num] = {
            'curr': int(line_decomp[11][:-1]),
            'total': int(line_decomp[3])
        }
        positions.append(cog_num)

    new_cog_num = cog_num+1
    cogs[new_cog_num] = {
        'curr': 0,
        'total': 11
    }
    positions.append(new_cog_num)

    time_released = 0
    curr_time = 0

    while True:
        curr_time += 1

        if curr_time == len(positions):
            break

        if positions[curr_time] != 0:
            cog_num = positions[curr_time]
            if not check_for_collision(cogs, cog_num,
                                       time_released + curr_time):
                curr_time = 0
                time_released += 1

    print time_released
