from adventlib import inpath, Vector
from adventlib.intcode import Computer

dirs = {(0, -1): 1, (0, 1): 2, (-1, 0): 3, (1, 0): 4}
wall, floor, oxygen = range(3)

class Square:

    def __init__(self, kind):
        self.kind = kind
        self.reset()

    def reset(self):
        self.complete = self.kind == wall

class Path:

    def __init__(self, p):
        self.v = [p]
        self.lookup = {p}

    def add(self, p):
        self.v.append(p)
        self.lookup.add(p)

    def pop(self):
        p = self.v.pop()
        self.lookup.remove(p)
        return p

def main():
    def select():
        steps = [p for d in dirs for p in [droid + d] if p not in path.lookup]
        for p in steps:
            if p not in chart:
                return p
        for p in steps:
            if not chart[p].complete:
                return p
        chart[droid].complete = True
        if 1 != len(path.v):
            path.pop()
            return path.pop()
    pipe = []
    i = iter(Computer(map(int, inpath().read_text().split(',')), pipe))
    droid = Vector([0, 0])
    path = Path(droid)
    chart = {droid: Square(floor)}
    while True:
        step = select()
        pipe.append(dirs[step - droid])
        kind = next(i)
        if step not in chart:
            chart[step] = Square(kind)
        if kind != wall:
            droid = step
            path.add(step)
        if kind == oxygen:
            break
    for square in chart.values():
        square.reset()
    path = Path(droid)
    maxpath = 1
    while True:
        step = select()
        if step is None:
            break
        pipe.append(dirs[step - droid])
        kind = next(i)
        if step not in chart:
            chart[step] = Square(kind)
        if kind != wall:
            droid = step
            path.add(step)
            maxpath = max(maxpath, len(path.v))
    print(maxpath - 1)
