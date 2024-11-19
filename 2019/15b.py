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

    def __init__(self):
        self.v = []
        self.lookup = set()

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
        path.pop()
        if path.v:
            return path.pop()
    droid = Vector([0, 0])
    chart = {droid: Square(floor)}
    path = Path()
    pipe = []
    i = iter(Computer(map(int, inpath().read_text().split(',')), pipe))
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
    path = Path()
    n = 0
    for s in chart.values():
        s.reset()
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
            n = max(n, len(path.v))
    print(n)
