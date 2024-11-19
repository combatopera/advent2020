from adventlib import inpath, Vector
from adventlib.intcode import Computer

dirs = {(0, -1): 1, (0, 1): 2, (-1, 0): 3, (1, 0): 4}
wall, floor, oxygen = range(3)

class Square:

    def __init__(self, kind):
        self.complete = kind == wall
        self.kind = kind

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
        if step not in chart:
            chart[step] = Square(kind)
        if kind != wall:
            droid = step
            path.append(step)
        if kind == oxygen:
            break
    print(len(path) - 1)
