
from termcolor import cprint


SAMPLES = """
   .^^.^.^^^^
"""

SAFE = '.'
TRAP = '^'

ROWS = 40


def part_one(input):
    cprint("Day 18: part one ", 'green')

    grid = []

    for line in input.splitlines():
        if not line:
            continue
        row = line.lstrip()
        grid.append(row)

    for i in range(ROWS-1):
        new_row = ''
        temp_row = '.' + grid[i] + '.'

        for group in [(temp_row[j], temp_row[j+1], temp_row[j+2])
                      for j in range(0, len(temp_row)-2)]:

            if (
            (group[0] == TRAP and group[1] == TRAP and group[2] == SAFE) or
            (group[0] == SAFE and group[1] == TRAP and group[2] == TRAP) or
            (group[0] == SAFE and group[1] == SAFE and group[2] == TRAP) or
            (group[0] == TRAP and group[1] == SAFE and group[2] == SAFE)
            ):
                new_row += TRAP
            else:
                new_row += SAFE
        grid.append(new_row)

    print ''.join(grid).count(SAFE)


def part_two(input):
    cprint("Day 18: part two ", 'green')

    global ROWS
    ROWS = 400000

    part_one(input)
