from adventlib import inpath, Vector
from adventlib.intcode import Computer
from collections import defaultdict
from itertools import chain

plus = (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)
dirs = (0, -1), (1, 0), (0, 1), (-1, 0)

def _enc(sub):
    v = [ord(c) for c in f"{','.join(sub)}\n"]
    assert len(v) <= 21
    return v

def main():
    grid = {}
    x = y = 0
    for k in Computer(map(int, inpath().read_text().split(','))):
        if 10 == k:
            if x:
                w = x
                x = 0
                y += 1
        else:
            grid[x, y] = c = chr(k)
            try:
                direction = '^>v<'.index(c)
            except ValueError:
                pass
            else:
                robot = Vector([x, y])
            x += 1
    h = y
    #for y in range(h):
    #    print(''.join(grid[x, y] for x in range(w)))
    route = []
    while True:
        if '#' == grid.get(robot + dirs[(direction - 1) % 4]):
            turn = 'L'
            direction = (direction - 1) % 4
        elif '#' == grid.get(robot + dirs[(direction + 1) % 4]):
            turn = 'R'
            direction = (direction + 1) % 4
        else:
            break
        n = 0
        while '#' == grid.get(robot + dirs[direction]):
            n += 1
            robot += dirs[direction]
        route.append((turn, str(n)))
    subs = {}
    for sub in 'ABC':
        steps = defaultdict(list)
        for i, step in enumerate(route):
            if isinstance(step, tuple):
                steps[step].append(i)
        step = min(steps.items(), key = lambda t: len(t[1]))[0]
        i = j = 0
        try:
            while 1 == len({route[k + i - 1] for k in steps[step]}):
                i -= 1
        except IndexError:
            pass
        try:
            while 1 == len({route[k + j + 1] for k in steps[step]}):
                j += 1
        except IndexError:
            pass
        subs[sub] = sum(route[steps[step][0] + i:steps[step][0] + j + 1], ())
        for k in reversed(steps[step]):
            route[k + i:k + j + 1] = [sub]
    input = [*_enc(route), *chain(*map(_enc, subs.values())), *_enc('n')]
    program = list(map(int, inpath().read_text().split(',')))
    program[0] = 2
    for dust in Computer(program, input):
        pass
    print(dust)
