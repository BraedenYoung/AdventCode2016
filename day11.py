import re
import heapq
from collections import OrderedDict

import itertools
from itertools import combinations
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
    ('elerium generator', 'RG'),
    ('elerium-compatible microchip', 'EM'),
    ('dilithium generator', 'DG'),
    ('dilithium-compatible microchip', 'DM')

])


def part_one(input):
    cprint("Day 11: part one ", 'green')

    global devices

    building = []

    floor_count = 0
    for line in input.splitlines():
        line = line.lstrip()

        floor = []
        floor_count += 1
        floor.append('F%s' % floor_count)

        floor.append(ELEVATOR) if floor_count == 1 else floor.append(EMPTY)

        for device in devices.keys():
            if findPart(device)(line):
                floor.append(devices[device])
            else:
                floor.append(EMPTY)

        building.append(tuple(floor))

    building = tuple(building)

    print_building(building)

    evaluate(building)


def findPart(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def evaluate(building):

    heap = []
    initial_cost = 0

    heapq.heappush(heap, (initial_cost, building))
    cost_so_far = {building: initial_cost}

    while heap:

        _, building = heapq.heappop(heap)

        if is_complete(building):
            print cost_so_far[building]
            print building
            return

        current_floor = get_current_floor(building)
        parts_to_move = get_valid_parts(building, current_floor)

        floors_to_consider = []

        for parts in parts_to_move:

            upper_floor = current_floor + 1
            if upper_floor <= 3:
                new_building, _ = use_elevator(building,
                                               upper_floor,
                                               *parts)
                if new_building:
                    floors_to_consider.append(new_building)

            if len(parts) == 1 and should_move_down(building, current_floor):
                lower_floor = current_floor - 1
                if lower_floor >= 0:
                    new_building, _ = use_elevator(
                        building,
                        lower_floor,
                        *parts)
                    if new_building:
                        floors_to_consider.append(new_building)

        new_cost = cost_so_far[building] + 1
        for building in floors_to_consider:
            if building not in cost_so_far.keys():
                cost_so_far[building] = new_cost
                heapq.heappush(heap, (new_cost, building))


def should_move_down(building, current_floor):
    if current_floor == 0:
        return False
    elif current_floor == 1:
        if floor_empty(building[0]):
            return False
    elif current_floor == 2:
        if floor_empty(building[0]) and floor_empty(building[1]):
            return False
    return True


def floor_empty(floor):
    for device in floor[2:]:
        if device != EMPTY:
            return False
    return True


def get_valid_parts(building, current_floor):

    devices = get_current_devices(building, current_floor)
    return list(combinations(devices, 2)) + list(combinations(devices, 1))


def use_elevator(building, new_floor, first_part,
                 second_part=None):

    if not first_part:
        return None, None

    current_floor = get_current_floor(building)

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

    if (not floor_is_safe(remade_original_floor)):
        return None, None

    new_building = list(building)

    new_building[current_floor] = tuple(remade_original_floor)
    new_building[new_floor] = tuple(remade_new_floor)

    return tuple(new_building), new_floor


def floor_is_safe(floor):
    generators = []
    for part in floor[2:]:
        if 'G' in part:
            generators.append(part)

    if len(generators) == 0:
        return True

    is_safe = True
    for part in floor[2:]:
        if 'M' in part:
            element = part[0]
            part_matched = False
            for gen in generators:
                if gen[0] == element:
                    part_matched = True
            if not part_matched:
                return False

    return True


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


def is_complete(building):
    for i in range(0, len(building)-1):
        for j in range(2, len(building[i])):
            if building[i][j] != EMPTY:
                return False

    return True


def print_building(building):
    for floor in reversed(building):
        print floor


def part_two(input):
    cprint("Day 9: part two ", 'green')
    global devices

    building = []

    floor_count = 0
    for line in input.splitlines():
        line = line.lstrip()

        floor = []
        floor_count += 1
        floor.append('F%s' % floor_count)

        if floor_count == 1:
            line += (' An elerium generator. An elerium-compatible '
                    'microchip. A dilithium generator. '
                    'A dilithium-compatible microchip')

        floor.append(ELEVATOR) if floor_count == 1 else floor.append(EMPTY)

        for device in devices.keys():
            if findPart(device)(line):
                floor.append(devices[device])
            else:
                floor.append(EMPTY)

        building.append(tuple(floor))

    building = tuple(building)

    print_building(building)

    evaluate(building)
