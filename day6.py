import collections

from termcolor import cprint


SAMPLE = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""


def part_one(input):
    cprint("Day 6: part one ", 'green')

    samples = []
    for line in input.splitlines():
        line = line.lstrip()
        samples.append(line)

    transposed = map(list, zip(*samples))

    char_count = []
    for position in transposed:
        char_count.append(collections.Counter(
            ''.join(position)).most_common(1)[0][0])

    print ''.join(char_count)


def part_two(input):
    cprint("Day 6: part two ", 'green')

    samples = []
    for line in input.splitlines():
        line = line.lstrip()
        samples.append(line)

    transposed = map(list, zip(*samples))

    char_count = []

    for position in transposed:
        least_common = position[0]
        min_count = position.count(position[0])

        for char in position[1:]:
            curr_count = position.count(char)
            if min_count > curr_count:
                min_count = curr_count
                least_common = char

        char_count.append(least_common)

    print ''.join(char_count)
