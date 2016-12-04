from collections import OrderedDict
from collections import Counter

from termcolor import cprint


def part_one(input):
    cprint("Day 4: part one ", 'green')

    valid = []

    for line in input.splitlines():
        line = line.lstrip()

        input = line.split('-')

        section_id, err_corr = input.pop(-1).split('[')
        err_corr = err_corr[:-1]# remove brace

        chars = OrderedDict()

        check_str = ''.join(sorted(''.join(input)))
        counter = Counter(check_str)

        for c in check_str:
            if c not in chars:
                chars[c] = counter[c]

        check_sum = []
        check_vals = []
        for w in sorted(chars, key=chars.get, reverse=True):

            if len(check_vals) == 5:
                break

            check_vals.append(chars[w])

        for val in check_vals:
            for key, v in chars.iteritems():
                if v == val:
                    check_sum.append(key)
                    chars[key] = None
                    break

        if ''.join(check_sum) == err_corr:
            valid.append(section_id)

    print sum(map(int, valid))


def part_two(input):
    cprint("Day 4: part two ", 'green')

    for line in input.splitlines():
        line = line.lstrip()

        input = line.split('-')

        section_id, _ = input.pop(-1).split('[')

        input = ' '.join(input)

        result = []
        for c in input:

            if c == ' ':
                result.append(' ')
                continue

            result.append(cycle_letter(c, section_id))

        if ''.join(result) == 'northpole object storage':
            print section_id


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def cycle_letter(letter, shift):
    return ALPHABET[(ALPHABET.index(letter) + int(shift)) % 26]


def test(input):
    result = None
    return result