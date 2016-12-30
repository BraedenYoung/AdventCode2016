
from termcolor import cprint


SAMPLE = """
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
"""

REG = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'out': [0]}

INST = {
    'cpy': lambda x, y: set_register(y, x),
    'inc': lambda x: increment_register(x),
    'dec': lambda x: decrement_register(x),
    'jnz': lambda x, y: jump_to_line(x, y),
    'tgl': lambda prog, x: toggle(prog, x),
    'mul': lambda x, y, z: multiply(x, y, z),
    'out': lambda x: transmit(x)
}

current_line = 0

initialize = 151


#  151< <220 !221 !164
def part_one(input):
    cprint("Day 23: part one ", 'green')
    global REG, current_line, initialize

    program = []

    for line in input.splitlines():
        if not line:
            continue

        line_decomp = line.split(' ')
        program.append(line_decomp)


    for initial in range(0, 1000):
        try:
            run_program(program)
        except BadTransmission:
            initialize += 1
            REG = {'a': initialize, 'b': 0, 'c': 0, 'd': 0, 'out': []}
            current_line = 0
            continue


def run_program(program):
    global current_line
    while True:
        operation = program[current_line][0]
        if operation != 'tgl':
            INST[operation](*program[current_line][1:])
        else:
            program = INST[operation](program, *program[current_line][1:])

        if operation != 'jnz':
            current_line += 1

        if current_line >= len(program):
            break

        if current_line < 0:
            current_line = 0


def set_register(register, value_or_register):
    try:
        REG[register] = int(value_or_register)
    except (KeyError, ValueError):
        REG[register] = int(REG[value_or_register])


def increment_register(register):
    REG[register] += 1


def decrement_register(register):
    REG[register] -= 1


def jump_to_line(jump_check, jump_value):
    global current_line

    if jump_check.isalpha():
        jump_check = int(REG[jump_check])
    else:
        jump_check = int(jump_check)

    if jump_check <= 0:
        current_line += 1
        return

    if jump_value.isdigit() or jump_value.startswith('-'):
        jump_value = int(jump_value)
    else:
        jump_value = int(REG[jump_value])

    current_line += jump_value


def toggle(program, index):
    global current_line

    offset = current_line + REG[index]
    if offset >= len(program) or offset < 0:
        return program
    instruction = list(program[offset])

    if len(instruction) == 2:

        if instruction[0] == "inc":
            instruction[0] = "dec"
        else:
            instruction[0] = "inc"

    else:

        if instruction[0] == "jnz":
            instruction[0] = "cpy"
        else:
            instruction[0] = "jnz"

    program[offset] = instruction
    return program


def multiply(a, b, d):
    if type(b) != int and not b.isdigit():
        operand_1 = REG[b]
    else:
        operand_1 = int(b)
    if type(d) != int and not d.isdigit():
        operand_2 = REG[d]
    else:
        operand_1 = int(d)

    REG[a] += operand_1 * operand_2


def transmit(x):
    global current_line, initialize, REG
    if x.isalpha():
        x = int(REG[x])
    else:
        x = int(x)

    if REG['out'] and x == REG['out'][-1]:
       raise BadTransmission()

    REG['out'].append(x)


    cprint('%s : %s' % (initialize, REG['out']), 'red')


class BadTransmission(Exception):
    pass


def part_two(input):
    cprint("Day 23: part two ", 'green')

    program = []

    for line in input.splitlines():
        if not line:
            continue

        line_decomp = line.split(' ')
        program.append(line_decomp)

