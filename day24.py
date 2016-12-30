import heapq
from itertools import permutations

import sys
from termcolor import cprint


SAMPLE = """
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
"""

WALL = '#'
EMPTY = '.'
ROBOT = '@'

wires = []


def part_one(input):
    cprint("Day 22: part one ", 'green')

    global wires

    vent_map = []
    curr_pos = (0, 0)

    row = 0
    for line in input.splitlines():
        if not line:
            continue

        col = 0
        vent_row = []

        for col, char in enumerate(line):
            if char == WALL:
                vent_row.append(WALL)
            elif char == EMPTY:
                vent_row.append(EMPTY)
            elif char.isdigit():
                if char == '0':
                    curr_pos = (row, col)
                    vent_row.append(ROBOT)
                    continue
                vent_row.append(char)
                wires.append((row, col))

        vent_map.append(vent_row)
        row += 1

    print_map(vent_map)

    shortest = sys.maxint
    trip_costs = {}

    possible_trips = permutations(wires+[curr_pos])

    for trip_perm in possible_trips:

        start = curr_pos

        steps_in_perm = 0
        for goal in list(trip_perm):
            if goal == start:
                continue
            steps = trip_costs.get((start, goal))
            if not steps:
                    costs = find_path(vent_map, start, goal)
                    steps = costs[goal]
                    trip_costs[(start, goal)] = steps
                    trip_costs[(goal, start)] = steps
            steps_in_perm += steps
            start = goal

        shortest = min(shortest, steps_in_perm)

    print shortest


def find_path(vent_map, curr_pos, curr_goal):
    global wires

    heap = []

    heapq.heappush(heap, (0, (curr_pos, 0)))
    costs = {curr_pos: None}

    while heap:
        new_cost, args = heapq.heappop(heap)
        curr_pos, cost = args
        if curr_pos == curr_goal:
            break

        new_cost = cost + 1
        for next in get_neighbours(vent_map, curr_pos):
            cost_so_far = costs.get(next)

            if cost_so_far is None or new_cost < cost_so_far:
                costs[next] = new_cost
                priority = new_cost + heuristic(next, curr_goal)

                heapq.heappush(heap, (priority, (tuple(next), new_cost)))

    if not costs[curr_goal]:
        costs[curr_goal] = sys.maxint

    return costs


def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def get_neighbours(vent_map, pos):

    paths = []
    if pos[0] > 0 and vent_map[pos[0]-1][pos[1]] != WALL:
        paths.append((pos[0]-1, pos[1])) # UP
    if pos[0] < len(vent_map) and vent_map[pos[0]+1][pos[1]] != WALL:
        paths.append((pos[0]+1, pos[1])) # DOWN
    if pos[1] > 0 and vent_map[pos[0]][pos[1]-1] != WALL:
        paths.append((pos[0], pos[1]-1)) # LEFT
    if pos[1] < len(vent_map[pos[0]]) and vent_map[pos[0]][pos[1]+1] != WALL:
        paths.append((pos[0], pos[1]+1)) # Right

    return paths


def print_map(map):
    for row in map:
        for col in row:
            if col == EMPTY:
                cprint(col, 'white', end=''),
            elif col == ROBOT:
                cprint(col, 'green', end='')
            elif col.isdigit():
                cprint(col, 'magenta', end='')
            elif col == WALL:
                cprint(col, 'red', end='')

        print


def part_two(input):
    cprint("Day 22: part two ", 'green')

    global wires

    row = 0
    for line in input.splitlines():
        if not line:
            continue

        col = 0
        vent_row = []

        for col, char in enumerate(line):
            if char == WALL:
                vent_row.append(WALL)
            elif char == EMPTY:
                vent_row.append(EMPTY)
            elif char.isdigit():
                if char == '0':
                    curr_pos = (row, col)
                    vent_row.append(ROBOT)
                    continue
                vent_row.append(char)
                wires.append((row, col))

        vent_map.append(vent_row)
        row += 1

    print_map(vent_map)

    shortest = sys.maxint
    trip_costs = {}

    possible_trips = permutations(wires+[curr_pos])

    for trip_perm in possible_trips:
        start = curr_pos
        steps_in_perm = 0
        for goal in list(trip_perm):
            if goal == start:
                continue
            steps = trip_costs.get((start, goal))
            if not steps:
                    costs = find_path(vent_map, start, goal)
                    steps = costs[goal]
                    trip_costs[(start, goal)] = steps
                    trip_costs[(goal, start)] = steps
            steps_in_perm += steps
            start = goal

        steps = trip_costs.get((goal, curr_pos))
        if not steps:
            costs = find_path(vent_map, goal, curr_pos)
            steps = costs[goal]
        steps_in_perm += steps
        shortest = min(shortest, steps_in_perm)

    print shortest
