
from termcolor import cprint


SAMPLE = """X(8x2)(3x3)ABCY
A(2x2)BCD(2x2)EFG
(3x3)XYZ
"""


def part_one(input):
    cprint("Day 9: part one ", 'green')

    for line in input.splitlines():
        line = line.lstrip()

        index = 0
        while index != len(line):
            marker, index = find_next_marker(line, index)

            if not marker or index >= len(line):
                break

            line, index = eval_marker(marker, line, index)

        print len(line)


def find_next_marker(line, curr_index):

    start_index = 0
    final_index = len(line) - 1
    marker = ''

    for index in range(curr_index, final_index):
        if line[index] == '(':
            start_index = index
        elif line[index] == ')':
            marker = line[start_index:index+1]
            final_index = index + 1
            break

    return marker, final_index


def eval_marker(marker, line, index, include_repeated=False):
    seq_len, multi = map(int, marker[1:-1].split('x'))
    repeated = ''
    for _ in range(multi):
        repeated = repeated + line[index:index+seq_len]
    final_index = index - len(marker)
    if not include_repeated:
        final_index += len(repeated)
    result_line = line[:index-len(marker)] + repeated + line[index + seq_len:]
    return result_line, final_index


SAMPLE2 = """(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN
(27x12)(20x12)(13x14)(7x10)(1x12)A
X(8x2)(3x3)ABCY
"""


def part_two(input):
    cprint("Day 9: part two ", 'green')

    for line in input.splitlines():
        line = line.lstrip()

        print get_char_count(line)


def get_char_count(line):

    if not line:
        return 0

    marker, count, line = find_next_marker_with_count(line)

    if not marker:
        return count

    seq_len, multi = map(int, marker[1:-1].split('x'))
    result_multi = multi * get_char_count(line[:seq_len])

    return count + get_char_count(line[seq_len:]) + result_multi


def find_next_marker_with_count(line):

    final_index = len(line) - 1
    count = 0
    marker = ''

    for index in range(len(line)):
        if line[index] == '(':
            start_index = index
            while line[index] != ')':
                index += 1
            marker = line[start_index:index+1]
            final_index = index + 1
            break
        else:
            count += 1

    return marker, count, line[final_index:]
