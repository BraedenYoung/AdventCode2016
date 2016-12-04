
from termcolor import cprint


SAMPLE_TEXT = """
ULL
RRDDD
LURDL
UUUUD
"""


key_pad = [[1,2,3],
           [4,5,6],
           [7,8,9]]


def part_one(input):
    cprint("Day 2: part one ", 'green')

    curr_pos = (1,1) #5

    for line in input.splitlines():

        for dir in line:
            if dir == 'U':
                if curr_pos[0] != 0:
                    curr_pos = (curr_pos[0]-1, curr_pos[1])
            elif dir == 'D':
                if curr_pos[0] != 2:
                    curr_pos = (curr_pos[0]+1, curr_pos[1])
            elif dir == 'L':
                if curr_pos[1] != 0:
                    curr_pos = (curr_pos[0], curr_pos[1]-1)
            elif dir == 'R':
                if curr_pos[1] != 2:
                    curr_pos = (curr_pos[0], curr_pos[1]+1)

        print key_pad[curr_pos[0]][curr_pos[1]]


key_pad2 = [[0, 0, 1, 0, 0],
            [0, 2, 3, 4, 0],
            [5, 6, 7, 8, 9],
            [0, 'A','B','C', 0],
            [0, 0, 'D', 0, 0]]



def part_two(input):
    cprint("Day 2: part two ", 'green')

    curr_pos = (2, 0) #5

    for line in input.splitlines():
        for dir in line:
            if dir == 'U':
                if curr_pos[0] != 0 and key_pad2[curr_pos[0]-1][curr_pos[1]] != 0:
                    curr_pos = (curr_pos[0]-1, curr_pos[1])
            elif dir == 'D':
                if curr_pos[0] != len(key_pad2)-1 and key_pad2[curr_pos[0]+1][curr_pos[1]] != 0:
                    curr_pos = (curr_pos[0]+1, curr_pos[1])
            elif dir == 'L':
                if curr_pos[1] != 0 and key_pad2[curr_pos[0]][curr_pos[1]-1] != 0:
                    curr_pos = (curr_pos[0], curr_pos[1]-1)
            elif dir == 'R':
                if curr_pos[1] != len(key_pad2[curr_pos[1]])-1 and key_pad2[curr_pos[0]][curr_pos[1]+1] != 0:
                    curr_pos = (curr_pos[0], curr_pos[1]+1)

        print key_pad2[curr_pos[0]][curr_pos[1]]


def test(input):
    result = None
    return result
