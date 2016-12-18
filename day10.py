import operator
from termcolor import cprint


SAMPLE = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""

BOT_OPERATIONS = {}


def part_one(input):
    cprint("Day 10: part one ", 'green')


    curr_values = []
    bot_state = {}

    for line in input.splitlines():
        line = line.lstrip()

        separated_input = line.split(' ')
        destination_bot = separated_input[-1]

        if len(separated_input) == 6:
            value = separated_input[1]
            curr_values.append((destination_bot, value))

        else:
            high = (separated_input[-1] if separated_input[-2] == 'bot'
                   else '10'+separated_input[-1])
            low = (separated_input[6] if separated_input[5] == 'bot'
                   else '10'+separated_input[6])

            BOT_OPERATIONS[separated_input[1]] = (low, high)

    for bot, value in curr_values:
        bot_state = run_system(bot, value, bot_state)

    return bot_state


def run_system(bot, value, bot_state):
    if not bot or not value:
        return bot_state

    if bot not in bot_state or len(bot_state[bot]) <= 0:
        bot_state[bot] = [value,]
        return bot_state

    bot_state[bot].append(value)
    bot_state[bot] = map(int, bot_state[bot])
    bot_state[bot].sort()
    bot_state[bot] = map(int, bot_state[bot])

    if len(bot_state[bot]) == 1:
        return bot_state

    if '17' in bot_state[bot] and '61' in bot_state[bot]:
        print bot

    max = bot_state[bot].pop(1)
    min = bot_state[bot].pop(0)

    bot_state = run_system(BOT_OPERATIONS[bot][0], min, bot_state)
    bot_state = run_system(BOT_OPERATIONS[bot][1], max, bot_state)

    return bot_state


def part_two(input):
    cprint("Day 10: part two ", 'green')

    bot_state = part_one(input)
    result = reduce(operator.mul, map(int, [bot_state['100'][0],
                                            bot_state['101'][0],
                                            bot_state['102'][0]]
                                      )
                    )
    print ('%s x %s x %s = %s' % (bot_state['100'], bot_state['101'],
                                  bot_state['102'], result))
