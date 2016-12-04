
from termcolor import cprint


def part_one(input):
    cprint("Day 3: part one ", 'green')

    valid = 0

    for line in input.splitlines():
        line = line.lstrip()
        sides = map(int, line.split())
        if check_triangle(sides):
            valid = valid +1

    print valid


def check_triangle(sides):
    if sum(sides[:2]) > sides[2] and sum(sides[1:]) > sides[0] and (sides[0] + sides[2]) > sides[1]:
        return True
    return False


def part_two(input):
    cprint("Day 3: part two ", 'green')

    valid = 0
    three_lines = []

    for line in input.splitlines():
        line = line.lstrip()
        sides = map(int, line.split())
        three_lines.append(sides)

        if len(three_lines) == 3:
            for i in range(0,3):
                if check_triangle([three_lines[0][i], three_lines[1][i], three_lines[2][i]]):
                    valid = valid +1
            three_lines = []
            continue

    print valid


def test(input):
    result = None
    return result
