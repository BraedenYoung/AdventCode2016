
from termcolor import cprint


SAMPLE = """10
"""

DESTINATION = (31, 39)
SAMPLE_DESTINATION = (7,4)

fav_num = 0
smallest = 99999


def part_one(input):
    cprint("Day 13: part one ", 'green')

    for line in input.splitlines():
        global fav_num
        fav_num = int(line.lstrip())

    curr_pos = (1, 1)
    print len(path_count(curr_pos, [])) - 1


def path_count(curr_pos, path_taken):
    global smallest

    path_taken.append(curr_pos)

    if len(path_taken) - 1 > smallest:
        return

    if curr_pos == DESTINATION:
        if len(path_taken) - 1 < smallest:
            smallest = len(path_taken) - 1
        return path_taken

    possible_paths = get_paths(curr_pos, path_taken)

    shortest = []

    while True:
        if not possible_paths:
            break

        new_step = possible_paths.pop()

        if new_step not in path_taken:

            newpath = path_count(new_step, list(path_taken))

            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest


def get_paths(curr_pos, path_taken):
    paths = []

    up = (curr_pos[0], curr_pos[1]-1)
    right = (curr_pos[0]+1, curr_pos[1])
    down = (curr_pos[0], curr_pos[1]+1)
    left = (curr_pos[0]-1, curr_pos[1])

    for pos in [up, right, down, left]:
        if pos[0] < 0 or pos[1] < 0:
            continue

        if space_is_open(*pos) and pos not in path_taken:
                paths.append(pos)

    return paths


def space_is_open(x, y):
    global fav_num
    open_check = x*x + 3*x + 2*x*y + y + y*y + fav_num
    return bin(open_check).count('1') % 2 == 0


def part_two(input):
    cprint("Day 13: part two ", 'green')

    for line in input.splitlines():
        global fav_num
        fav_num = int(line.lstrip())

    curr_pos = (1, 1)
    visisted = [curr_pos]
    _, visisted = find_unique_coords(curr_pos, [], visisted)
    print len(visisted)


def find_unique_coords(curr_pos, path_taken, visited):
    path_taken.append(curr_pos)

    if len(path_taken) - 1 == 50:
        return path_taken, visited

    possible_paths = get_paths(curr_pos, path_taken)
    if possible_paths and visited:
        visited.extend(possible_paths)
        visited = set(visited)

    shortest = []

    while True:
        if not possible_paths:
            break

        new_step = possible_paths.pop()

        if new_step not in path_taken:

            newpath, visited = find_unique_coords(new_step, list(path_taken),
                                                  list(visited))

    return shortest, visited
