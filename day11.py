import copy
from collections import OrderedDict

import itertools
from termcolor import cprint


SAMPLE = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
"""


BOT_OPERATIONS = {}
EMPTY = '.'
ELEVATOR = 'E'

possible_solutions = []


def part_one(input):
    cprint("Day 11: part one ", 'green')

    input = SAMPLE

    building = []
    devices = OrderedDict([
        ('hydrogen generator', 'HG'),
        ('hydrogen-compatible microchip', 'HM'),
        ('lithium generator', 'LG'),
        ('lithium-compatible microchip', 'LM'),
        ('plutonium generator', 'PG'),
        ('plutonium-compatible microchip', 'PM'),
        ('promethium generator', 'PrG'),
        ('promethium-compatible microchip', 'PrM'),
        ('ruthenium generator', 'RG'),
        ('ruthenium-compatible microchip', 'RM'),
        ('strontium generator', 'SG'),
        ('strontium-compatible microchip', 'SM'),
        ('thulium generator', 'TG'),
        ('thulium-compatible microchip', 'TM'),
    ])

    floor_count = 0
    for line in input.splitlines():
        line = line.lstrip()

        floor = []
        floor_count += 1
        floor.append('F%s' % floor_count)

        floor.append(ELEVATOR) if floor_count == 1 else floor.append(EMPTY)

        for device in devices.keys():
            if device in line:
                floor.append(devices[device])
            else:
                floor.append(EMPTY)

        building.append(tuple(floor))

    print_building(building)

    evaluate(building, [])

    if len(possible_solutions) == 0:
        cprint('No Solutions Found', 'red')
        return

    print min(possible_solutions)


def evaluate(building, current_trip, parts_on_elev=None, dest_floor=None):
    if is_complete(building, current_trip):
        return None

    current_floor = get_current_floor(building)

    if dest_floor == current_floor:
        return

    if dest_floor and parts_on_elev:
        building, current_floor = use_elevator(building, current_floor,
                                               dest_floor, *parts_on_elev)

    parts_to_move = get_valid_parts(building, current_floor)

    if building[current_floor] in current_trip:
        return

    current_trip.append(tuple(building[current_floor]))

    if not parts_to_move:
        return None

    for parts in parts_to_move:

        dest_floor = current_floor + 1
        if dest_floor != current_floor and dest_floor <= 3:
            evaluate(copy.deepcopy(building), list(current_trip), parts,
                     dest_floor=dest_floor)

        if should_move_down(building, current_floor):

            dest_floor = current_floor - 1
            if dest_floor != current_floor and dest_floor >= 0:
                evaluate(copy.deepcopy(building), list(current_trip), parts,
                         dest_floor=dest_floor)

def should_move_down(building, current_floor):
    if current_floor > 1:
        for i in range(1):
            if not floor_empty(building[i]):
                return False
    return True

def floor_empty(floor):
    for device in floor[2:]:
        if device != EMPTY:
            return False
    return True

def load_elevator(part_1, part_2):
    if not part_1 and part_2:
        return False
    else:
        return True


def get_valid_parts(building, current_floor):
    parts = get_current_devices(building, current_floor)

    valid_parts = []

    for i, part in enumerate(parts):
        valid = True
        remaining_list = parts[:i]+parts[i+1:]

        for part_comb in list(itertools.combinations(remaining_list, 2)):
            if not compare_part(*part_comb):
                valid = False

        if valid:
            valid_parts.append((part,))

    if current_floor == 3:
        return valid_parts

    for part_comb in list(itertools.combinations(parts, 2)):
        valid = True

        temp = list(parts)
        del temp[temp.index(part_comb[0])]
        del temp[temp.index(part_comb[1])]

        for part_comb_inner in list(itertools.combinations(temp, 2)):
            if not compare_part(*part_comb_inner):
                valid = False

        if valid:
            valid_parts.append(part_comb)

    return valid_parts


def use_elevator(building, current_floor, new_floor, first_part,
                 second_part=None):

    remade_original_floor = list(building[current_floor])
    remade_new_floor = list(building[new_floor])

    first_index = building[current_floor].index(first_part)
    remade_original_floor[first_index] = EMPTY
    part_1 = building[current_floor][first_index]
    remade_new_floor[first_index] = part_1

    if second_part:
        second_index = building[current_floor].index(second_part)
        part_2 = building[current_floor][second_index]
        remade_original_floor[second_index] = EMPTY
        remade_new_floor[second_index] = part_2

    remade_original_floor[1] = EMPTY
    remade_new_floor[1] = ELEVATOR

    building[current_floor] = tuple(remade_original_floor)
    building[new_floor] = tuple(remade_new_floor)

    return building, new_floor


def compare_part(part_1, part_2):
    if part_1[-1] == part_2[-1]:
        return True
    elif part_1[0] == part_2[0]:
        return True
    return False


def get_current_devices(building, current_floor):
    curr_dev = []
    for i in range(2, len(building[current_floor])):
        if building[current_floor][i] != '.':
            curr_dev.append(building[current_floor][i])
    return curr_dev


def get_current_floor(building):
    for num, floor in enumerate(building):
        if floor[1] == 'E':
            return num


def is_complete(building, current_trip):
    for i in range(1, len(building)):
        for j in range(2, len(building[i])):
            if building[i][j] != EMPTY:
                return False

    possible_solutions.append(current_trip)
    print possible_solutions
    return True


def print_building(building):
    for floor in reversed(building):
        print floor


def part_two(input):
    cprint("Day 9: part two ", 'green')

    for line in input.splitlines():
        line = line.lstrip()
