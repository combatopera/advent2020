from adventlib import inpath, Ring, Vector
from adventlib.intcode import Computer
from collections import defaultdict
from itertools import chain

plus = (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)

def _enc(routine):
    v = list(map(ord, f"{','.join(routine)}\n"))
    assert len(v) <= 21
    return v

def main():
    grid = {}
    x = y = 0
    program = list(map(int, inpath().read_text().split(',')))
    for k in Computer(program):
        if 10 == k:
            x = 0
            y += 1
        else:
            grid[x, y] = c = chr(k)
            try:
                direction = '^>v<'.index(c)
            except ValueError:
                pass
            else:
                dirs = Ring([(0, -1), (1, 0), (0, 1), (-1, 0)]).rol(direction)
                robot = Vector([x, y])
            x += 1
    route = []
    while True:
        if '#' == grid.get(robot + dirs[-1]):
            turn = 'L'
            dirs.rol(-1)
        elif '#' == grid.get(robot + dirs[1]):
            turn = 'R'
            dirs.rol(1)
        else:
            break
        n = 0
        while '#' == grid.get(robot + dirs[0]):
            n += 1
            robot += dirs[0]
        route.append((turn, str(n)))
    subs = []
    for sub in 'ABC':
        steps = defaultdict(list)
        for i, step in enumerate(route):
            if not isinstance(step, str):
                steps[step].append(i)
        step, indices = min(steps.items(), key = lambda t: len(t[1]))
        i = j = 0
        try:
            while 1 == len({route[k + i - 1] for k in indices}):
                i -= 1
        except IndexError:
            pass
        try:
            while 1 == len({route[k + j + 1] for k in indices}):
                j += 1
        except IndexError:
            pass
        subs.append(list(chain(*route[indices[0] + i:indices[0] + j + 1])))
        for k in reversed(indices):
            route[k + i:k + j + 1] = [sub]
    for dust in Computer([2] + program[1:], [*_enc(route), *chain(*map(_enc, subs)), *_enc('n')]):
        pass
    print(dust)
