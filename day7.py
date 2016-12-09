
from termcolor import cprint

import re


SAMPLE = """riicbbctoem[zvvfukltptxfcxazyi]ybrstbqfckhzpyin"""


def part_one(input):
    cprint("Day 7: part one ", 'green')

    count = 0

    for line in input.splitlines():

        line = line.lstrip()

        if check_valid_part1(line):
            count += 1

    print count


def check_valid_part1(str):
    has_abba = False
    for i, char in enumerate(str):
        if not len(str) >= i+4:
            break

        current_char = str[i]
        following = str[i+1]

        if (following == str[i+2] and current_char == str[i+3]
            and current_char != following):
            if check_not_hypernet(str, i):
                has_abba = True
            else:
                return False

    if has_abba:
        return True

    return False


SAMPLE_2 = 'xyxaba[xy]xyx[vababddd]'


def part_two(input):
    cprint("Day 7: part two ", 'green')

    count = 0

    babs_regex = re.compile(r'\[(.*?)\]', re.IGNORECASE)

    for line in input.splitlines():
        line = line.lstrip()

        if check_valid_part2(line, babs_regex):
            count += 1

    print count


def check_valid_part2(str, babs_regex):

    has_aba = False

    curr_babs = babs_regex.findall(str)

    for i, char in enumerate(str):
        if not len(str) >= i+3:
            break

        current_char = str[i]
        following = str[i+1]

        if (current_char == str[i+2]
            and current_char != following):
            if check_not_hypernet(str, i, curr_babs):
                has_aba = True

    if has_aba:
        return True

    return False


def check_not_hypernet(str, index, curr_babs=None):
    for i in range(index, 0, -1):
        if str[i] == ']':
            break
        elif str[i] == '[':
            return False

    for i in range(index, len(str)):
        if str[i] == '[':
            break
        elif str[i] == ']':
            return False

    if curr_babs:
        return check_bab(str, index, curr_babs)

    return True


def check_bab(str, index, curr_babs):
    expected_bab = str[index+1] + str[index] + str[index+1]
    for bab in curr_babs:
        if expected_bab in bab:
            return True
    return False