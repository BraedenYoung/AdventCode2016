

def part_one(input):

    loc = [0,0]
    curr_dir = 0 #0n, 1e, 2s, -1w

    for d in input.split(', '):

        direction = d[0]
        d = d.replace(d[:1], '')

        dist = int(d)

        if direction == 'L':
            curr_dir = change_dir(curr_dir, -1)
        elif direction == 'R':
            curr_dir = change_dir(curr_dir, 1)

        if curr_dir == 0:
            loc[1] = loc[1] + dist
        elif curr_dir == 1:
            loc[0] = loc[0] + dist
        elif curr_dir == 2: # S
            loc[1] = loc[1] - dist
        elif curr_dir == -1: # w
            loc[0] = loc[0] - dist

    result = sum([abs(loc[0]), abs(loc[1])])
    print result

def change_dir(curr_dir, change):
    if change == -1: #L
        if curr_dir == -1:
            curr_dir = 2
        else:
            curr_dir = curr_dir - 1
    elif change == 1: #R
        if curr_dir == 2:
            curr_dir = -1
        else:
            curr_dir = curr_dir + 1

    return curr_dir


def part_two(input):

        prev = []

        loc = [0,0]
        curr_dir = 0 #0n, 1e, 2s, -1w

        done = False

        for d in input.split(', '):

            direction = d[0]

            d = d.replace(d[:1], '')
            dist = int(d)

            if direction == 'L':
                curr_dir = change_dir(curr_dir, -1)
            elif direction == 'R':
                curr_dir = change_dir(curr_dir, 1)

            if curr_dir == 0:
                for _ in range(dist):
                    loc[1] = loc[1] + 1
                    if loc in prev:
                        done = True
                        break
                    prev.append(list(loc))
            elif curr_dir == 1:
                for _ in range(dist):
                    loc[0] = loc[0] + 1
                    if loc in prev:
                        done = True
                        break
                    prev.append(list(loc))
            elif curr_dir == 2: # S
                for _ in range(dist):
                    loc[1] = loc[1] - 1
                    if loc in prev:
                        done = True
                        break
                    prev.append(list(loc))
            elif curr_dir == -1: # w
                for _ in range(dist):
                    loc[0] = loc[0] - 1
                    if loc in prev:
                        done = True
                        break
                    prev.append(list(loc))

            if done:
                print sum([abs(loc[0]), abs(loc[1])])
                break

        print loc
        result = sum([abs(loc[0]), abs(loc[1])])

        print result
        return result


def test(input):
    result = None
    return result
