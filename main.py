import time
from termcolor import cprint
import requests
import sys


DAY = 4

def main():

    from day4 import part_one, part_two, test

    exercise = sys.argv[2]
    first_run = sys.argv[3]

    cprint("Part %s for day %s" % (exercise, DAY), 'magenta')

    if first_run == '1':
        cprint("FIRST RUN", 'red')

    input_text = handle_input(first_run)

    start = time.time()
    if exercise == '1':
        part_one(input_text)
    elif exercise == '2':
        part_two(input_text)
    else:
        test_input = ''
        test(test_input)

    cprint("Process time: %s" % (time.time() - start), 'yellow')


def handle_input(first_run):
    if first_run == '1':
        r = requests.get(
            'http://adventofcode.com/2016/day/{day}/input'.format(day=DAY),
            cookies=dict(session=sys.argv[4]))
        print r.text
        input_text = r.text
        with open('input.txt', 'w') as input_file:
            input_file.write(input_text)
    else:
        with open('input.txt', 'r') as input_file:
            input_text = input_file.read()
    return input_text


if __name__ == '__main__':
    main()
