
from termcolor import cprint


SAMPLE = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""

REG = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

INST = {
    'cpy': lambda x, y: set_register(y, x),
    'inc': lambda x: increment_register(x),
    'dec': lambda x: decrement_register(x),
    'jnz': lambda x, y: jump_to_line(x, y),
}

current_line = 0


def part_one(input):
    cprint("Day 12: part one ", 'green')

    program = []

    for line in input.splitlines():
        line = line.lstrip()

        line_decomp = line.split(' ')
        program.append(line_decomp)

    run_program(program)
    print REG


def run_program(program):
    global current_line
    while True:
        operation = program[current_line][0]
        INST[operation](*program[current_line][1:])

        if operation != 'jnz':
            current_line += 1

        if current_line >= len(program):
            break

        if current_line < 0:
            current_line = 0


def set_register(register, value_or_register):
    if value_or_register.isdigit():
        REG[register] = int(value_or_register)
    else:
        REG[register] = int(REG[value_or_register])


def increment_register(register):
    REG[register] += 1


def decrement_register(register):
    REG[register] -= 1


def jump_to_line(jump_check, jump_value):
    global current_line

    if (not jump_check.isdigit() and int(REG[jump_check]) == 0) or jump_check == 0:
        current_line += 1
        return

    current_line += int(jump_value)


def part_two(input):
    cprint("Day 12: part two ", 'green')

    REG['c'] = 1
    part_one(input)
