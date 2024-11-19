from adventlib import inpath, Vector
from adventlib.intcode import Computer

dirs = {(0, -1): 1, (0, 1): 2, (-1, 0): 3, (1, 0): 4}
wall, floor, oxygen = range(3)

class Square:

    icons = {wall: '#', floor: ' ', oxygen: '$'}

    def __init__(self, kind):
        self.complete = kind == wall
        self.kind = kind

    def __str__(self):
        return self.icons[self.kind]

def main():
    def select():
        steps = [p for d in dirs for p in [droid + d] if p not in path]
        for p in steps:
            if p not in chart:
                return p
        for p in steps:
            if not chart[p].complete:
                return p
        chart[droid].complete = True
        path.pop()
        return path.pop()
    droid = Vector([0, 0])
    chart = {droid: Square(floor)}
    path = [droid]
    pipe = []
    i = iter(Computer(map(int, inpath().read_text().split(',')), pipe))
    while True:
        step = select()
        pipe.append(dirs[step - droid])
        kind = next(i)
        if kind == oxygen:
            print(len(path))
            break
        if step not in chart:
            chart[step] = Square(kind)
        if kind != wall:
            droid = step
            path.append(step)
        minx = min(p[0] for p in chart)
        maxx = max(p[0] for p in chart)
        miny = min(p[1] for p in chart)
        maxy = max(p[1] for p in chart)
        for y in range(miny, maxy + 1):
            print(''.join('@' if (x, y) == droid else '*' if (x, y) == (0, 0) else str(chart[x, y]) if (x, y) in chart else '/' for x in range(minx, maxx + 1)))
