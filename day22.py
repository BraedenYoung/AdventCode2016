
from itertools import product

from termcolor import cprint


SAMPLE = """
Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%
"""


def part_one(input):
    cprint("Day 22: part one ", 'green')

    nodes = []
    for line in input.splitlines():
        if not line:
            continue

        if line[0] != '/':
            continue

        line_decomp = line.lstrip().split(' ')

        node = tuple(map(lambda val: int(val[1:]),
                         line_decomp.pop(0).split('-')[1:]))
        sizes = []
        for val in line_decomp:
            if val == '':
                continue
            sizes.append(val)

        size, used, free, use = map(lambda val: int(val[:-1]), sizes)
        nodes.append((node, (size, used, free, use)))

    print get_viable(nodes)


def get_viable(nodes):
    count = 0
    for comb in product(nodes, repeat=2):
        if comb[0] == comb[1] or comb[0][1][1] == 0:
            continue

        if comb[0][1][1] <= comb[1][1][2]:
            count += 1

    return count


TOO_LARGE = ('##', '##', '##', '##')
count = 0


def part_two(input):
    cprint("Day 22: part two ", 'green')

    nodes = {}
    highest_x = 0
    empty_pos = (0, 0)

    for line in input.splitlines():
        if not line:
            continue

        if line[0] != '/':
            continue

        line_decomp = line.lstrip().split(' ')

        node = tuple(map(lambda val: int(val[1:]),
                         line_decomp.pop(0).split('-')[1:]))
        sizes = []
        for val in line_decomp:
            if val == '':
                continue
            sizes.append(val)

        size, used, free, use = map(lambda val: int(val[:-1]), sizes)

        if used == 0:
            empty_pos = node

        args = (size, used, free, use)
        if size > 100 and (size - used) < 100:
            args = TOO_LARGE

        nodes[node] = args

        if node[0] > highest_x:
            highest_x = node[0]

    bring_empty_to_top(nodes, empty_pos, highest_x)

    global count
    print count + 1 + 5 * (highest_x -1)


def bring_empty_to_top(nodes, empty, highest):
    while True:
        if empty[1] == 0:
            break

        new_empty = None
        if nodes[(empty[0], empty[1]-1)] == TOO_LARGE:
            while empty != (empty[0], empty[1]-1):
                new_empty = (empty[0]-1, empty[1])
                nodes = move_drive(nodes, empty, new_empty)
                empty = new_empty
                if nodes[(empty[0], empty[1]-1)] != TOO_LARGE:
                    break
        else:
            new_empty = (empty[0], empty[1]-1)
            nodes = move_drive(nodes, empty, new_empty)

        empty = new_empty

    while True:
        if empty == (highest-1, 0):
            break
        new_empty = (empty[0]+1, empty[1])
        nodes = move_drive(nodes, empty, new_empty)
        empty = new_empty

    return nodes, empty


def move_drive(nodes, first, second):
    global count
    count += 1
    nodes[first], nodes[second] = nodes[second], nodes[first]
    return nodes


def print_nodes(nodes, highest):
    for y in range(highest+1):
        for x in range(highest+1):
            try:
                print '| (%s / %s) ' % (nodes[(x, y)][1] or
                                        '_', nodes[(x, y)][0]),
            except KeyError:
                break

        print ''
