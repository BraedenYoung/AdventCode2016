import re
from termcolor import cprint
from itertools import permutations
perms = [''.join(p) for p in permutations('stack')]


SAMPLES = """
   swap position 4 with position 0
   swap letter d with letter b
   reverse positions 0 through 4
   rotate left 1 step
   move position 1 to position 4
   move position 3 to position 0
   rotate based on position of letter b
   rotate based on position of letter d
"""


INST = {
    'swap': lambda password, x, y: swap(password, x, y),
    'rotate': lambda password, dir, x: rotate(password, dir, x),
    'move': lambda password, x, y: move(password, x, y),
    'reverse': lambda password, start, end: reverse(password, start, end),
}


def part_one(input):
    cprint("Day 21: part one ", 'green')

    password = 'abcdefgh'

    digit_regex = re.compile(r'(\d)+')
    letter_regex = re.compile(r'\s([a-z])\s')
    dir_regex = re.compile((r'(left|right)'))

    for line in input.splitlines():
        if not line:
            continue

        line = line + ' '
        line_decomp = line.lstrip().split(' ')
        op = line_decomp[0]

        positions = digit_regex.findall(line)
        letters = map(lambda letter: letter.strip(), letter_regex.findall(line))

        dir = dir_regex.findall(line) or ['right'] if op == 'rotate' else []
        args = dir + positions + letters

        password = INST[op](password, *args)

    print password


def swap(password, x, y):
    if x.isdigit():
        x, y = sorted(map(int, (x, y)))
        return ''.join((password[:x], password[y], password[x+1:y],
                        password[x], password[y+1:]))
    return password.replace(x, '.').replace(y, x).replace('.', y)


def rotate(password, dir, x):
    password = list(password)
    if not x.isdigit():
        x = password.index(x) + 1
        if x > 4:
            x += 1

    x = int(x)
    if dir == 'right':
        return ''.join(password[-x % len(password):] + password[:-x % len(password)])
    return ''.join(password[x:] + password[:x])


def move(password, x, y):
    x, y = map(int, (x, y))
    password = list(password)
    if x < y:
        y += 1
    password.insert(y, password[x])
    if x > y:
        x += 1
    password.pop(x)
    return ''.join(password)


def reverse(password, start, end):
    start, end = sorted(map(int, (start, end)))
    return password[:start] + password[start:end+1][::-1] + password[end+1:]


def part_two(input):
    cprint("Day 21: part two ", 'green')

    digit_regex = re.compile(r'(\d)+')
    letter_regex = re.compile(r'\s([a-z])\s')
    dir_regex = re.compile((r'(left|right)'))

    for password in [''.join(p) for p in permutations('abcdefgh')]:
        curr = password
        for line in input.splitlines():
            if not line:
                continue

            line = line + ' '
            line_decomp = line.lstrip().split(' ')
            op = line_decomp[0]

            positions = digit_regex.findall(line)
            letters = map(lambda letter: letter.strip(), letter_regex.findall(line))

            dir = dir_regex.findall(line) or ['right'] if op == 'rotate' else []
            args = dir + positions + letters

            password = INST[op](password, *args)

        if password == 'fbgdceah':
            print curr
            break
