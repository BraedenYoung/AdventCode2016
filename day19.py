from math import floor

from termcolor import cprint


SAMPLES = """
    3
    5
    7
"""


def part_one(input):
    cprint("Day 19: part one ", 'green')

    elves = []

    for line in input.splitlines():
        if not line:
            continue
        party_size = int(line)

        for elf in range(1, party_size+1):
            elves.append((elf, 1))

        print white_elephant(elves)


def white_elephant(elves):

    curr_elf = 0

    while True:
        something_stolen = False

        victim_elf = curr_elf
        while True:

            victim_elf += 1
            victim_elf = victim_elf % len(elves)

            if victim_elf < curr_elf and victim_elf != 0:
                curr_elf += 1

            elves[curr_elf] = (elves[curr_elf][0],
                               elves[curr_elf][1] + elves[victim_elf][1])

            elves.pop(victim_elf)
            something_stolen = True
            break

        curr_elf += 1
        if curr_elf >= len(elves):
            curr_elf = 0

        if not something_stolen or len(elves) == 1:
            break

    for elf in elves:
        if elf[1] > 0:
            return elf[0]


def part_two(input):
    cprint("Day 19: part two ", 'green')

    elves = []

    for line in input.splitlines():
        if not line:
            continue
        party_size = int(line)

        for elf in range(1, party_size+1):
            elves.append((elf, 1))

        print white_elephant_across(elves)


def white_elephant_across(elves):

    curr_elf = 0

    while True:
        something_stolen = False

        while True:

            victim_elf = int(floor(len(elves) / 2))
            victim_elf = (curr_elf + victim_elf) % len(elves)

            try:
                elves[curr_elf] = (elves[curr_elf][0],
                                   elves[curr_elf][1] + elves[victim_elf][1])
            except IndexError:
                print '%s : %s : %s' % (len(elves), curr_elf, victim_elf)

            if victim_elf < curr_elf:
                curr_elf -= 1

            elves.pop(victim_elf)
            something_stolen = True
            break

        curr_elf += 1
        if curr_elf >= len(elves):
            curr_elf = 0

        if not something_stolen or len(elves) == 1:
            break

    for elf in elves:
        if elf[1] > 0:
            return elf[0]
