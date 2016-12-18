
import hashlib
import heapq

from termcolor import cprint


#########
#S| | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |
####### V

SAMPLES = """
    ulqzkmiv
    kglvqrro
    ihgpwlah
"""


DIRECTIONS = {0:'U',
              1:'D',
              2:'L',
              3:'R'}


def part_one(input):
    cprint("Day 17: part one ", 'green')

    pos = (0, 0)

    for line in input.splitlines():
        if not line:
            continue
        passcode = line


    heap = []
    cost = 0
    heapq.heappush(heap, (cost, (str(passcode), tuple(pos))))

    valut_reached = False

    while heap:
        new_cost, args = heapq.heappop(heap)
        passcode, pos = args

        if pos == (3, 3):
            valut_reached = True
            break
        cost += 1

        room_state = hashlib.md5(passcode).hexdigest()[:4]
        for direction, char in enumerate(room_state):
            if (not door_open(char) or
                (direction == 0 and pos[0] == 0) or
                (direction == 1 and pos[0] == 3) or
                (direction == 2 and pos[1] == 0) or
                (direction == 3 and pos[1] == 3)):
                continue

            new_passcode = passcode + DIRECTIONS[direction]
            new_pos = update_position(pos, direction)
            heapq.heappush(heap, (cost, (new_passcode, new_pos)))

    if valut_reached:
        cprint('Solution Found: %s ' % passcode, 'magenta')
    else:
        cprint('No Solutions', 'red')

def update_position(pos, direction):
    if direction == 0:
        return (pos[0] - 1, pos[1])
    elif direction == 1:
        return (pos[0] + 1, pos[1])
    elif direction == 2:
        return (pos[0], pos[1] - 1)
    elif direction == 3:
        return (pos[0], pos[1] + 1)


def door_open(char):
    if char in ('b', 'c', 'd', 'e', 'f'):
        return True
    return False


def part_two(input):
    cprint("Day 17: part two ", 'green')

    pos = (0, 0)

    for line in input.splitlines():
        if not line:
            continue
        line.lstrip()
        passcode = line

    heap = []
    cost = 0
    heapq.heappush(heap, (cost, (str(passcode), tuple(pos))))

    valut_reached = False

    solutions = []

    while heap:
        new_cost, args = heapq.heappop(heap)
        passcode, pos = args

        if pos == (3, 3):
            solutions.append(passcode)
            valut_reached = True
            continue

        cost += 1

        room_state = hashlib.md5(passcode).hexdigest()[:4]
        for direction, char in enumerate(room_state):
            if (not door_open(char) or
                    (direction == 0 and pos[0] == 0) or
                    (direction == 1 and pos[0] == 3) or
                    (direction == 2 and pos[1] == 0) or
                    (direction == 3 and pos[1] == 3)):
                continue

            new_passcode = passcode + DIRECTIONS[direction]
            new_pos = update_position(pos, direction)
            heapq.heappush(heap, (cost, (new_passcode, new_pos)))

    path_len = max(solutions, key=len)[len(input):]

    if valut_reached:
        cprint('Solution Found: %s ' % len(path_len), 'magenta')
    else:
        cprint('No Solutions', 'red')
