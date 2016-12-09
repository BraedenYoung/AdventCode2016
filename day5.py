
from termcolor import cprint
import hashlib


def part_one(input):
    cprint("Day 5: part one ", 'green')

    door_id = input
    print door_id

    index = 0

    password = []

    while True:
        hash_lib = hashlib.md5()
        hash_lib.update('%s%s' % (door_id, index))
        if hash_lib.hexdigest()[:5] == '00000':
            password.append(hash_lib.hexdigest()[5])
        if len(password) == 8:
            print ''.join(password)
            break
        index += 1
        hash_lib.update(door_id)


def part_two(input):
    cprint("Day 5: part two ", 'green')

    door_id = input

    index = 0

    password = {0:None,
                1:None,
                2:None,
                3:None,
                4:None,
                5:None,
                6:None,
                7:None}

    while True:
        hash_lib = hashlib.md5()
        hash_lib.update('%s%s' % (door_id, index))
        digest = hash_lib.hexdigest()
        if digest[:5] == '00000':
            position = digest[5]
            if int(position, 16) < 8:
                if not password[int(position, 16)]:
                    password[int(position, 16)] = hash_lib.hexdigest()[6]
        if not None in password.values():
            print ''.join(password.values())
            break
        index += 1
        hash_lib.update(door_id)
