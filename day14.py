import hashlib
import re

from termcolor import cprint


SAMPLE = """abc
"""


def part_one(input):
    cprint("Day 14: part one ", 'green')

    trips_regex = re.compile(r'.*?([0-9a-f])\1\1.*', re.IGNORECASE)
    quintuples_regex = re.compile(r'.*([0-9a-f])\1\1\1\1.', re.IGNORECASE)

    for line in input.splitlines():
        salt = line

    keys = []
    index = 0

    while True:
        if len(keys) == 64:
            break

        index += 1

        seed = ('%s%s' % (salt, str(index)))
        possible_key = hashlib.md5(seed).hexdigest()

        triple_chars = trips_regex.findall(possible_key)

        if triple_chars:
            is_valid = False
            for i in range(index+1, index + 1000):
                if is_valid:
                    break

                seed = ('%s%s' % (salt, str(i)))
                check_key = hashlib.md5(seed).hexdigest()

                quin_char = quintuples_regex.findall(check_key)

                if quin_char:
                    for c in quin_char:
                        if c in triple_chars:

                            keys.append(possible_key)
                            is_valid = True
                            break
    print index


def part_two(input):
    cprint("Day 14: part two ", 'green')

    trips_regex = re.compile(r'.*?([0-9a-f])\1\1.*', re.IGNORECASE)
    quintuples_regex = re.compile(r'.*([0-9a-f])\1\1\1\1.', re.IGNORECASE)

    for line in input.splitlines():
        salt = line

    keys = []
    index = 0

    while True:
        if len(keys) == 64:
            break

        index += 1

        seed = ('%s%s' % (salt, str(index)))
        possible_key = hashlib.md5(seed).hexdigest()
        for _ in range(2015):
            possible_key = hashlib.md5(possible_key).hexdigest()

        triple_chars = trips_regex.findall(possible_key)

        if triple_chars:
            is_valid = False
            for i in range(index + 1, index + 1000):
                if is_valid:
                    break

                seed = ('%s%s' % (salt, str(i)))

                check_key = hashlib.md5(seed).hexdigest()

                quin_char = quintuples_regex.findall(check_key)

                if quin_char:
                    for c in quin_char:
                        if c in triple_chars:

                            cprint("%s : %s" % (index, possible_key), 'green')
                            cprint("%s : %s" % (i, check_key), 'blue')

                            keys.append(possible_key)
                            is_valid = True
                            break

    print index
