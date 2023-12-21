from adventlib import inpath, Vector

dirs = (1, 0), (0, 1), (-1, 0), (0, -1)

class Farm:

    def __init__(self, lines):
        self.rocks = set()
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                if '#' == c:
                    self.rocks.add((x, y))
                elif 'S' == c:
                    self.start = Vector([x, y])
        self.size = x + 1, y + 1

    def newfront(self, oldfront, front):
        def g():
            for t in front:
                for d in dirs:
                    u = t + d
                    if not (u % self.size in self.rocks or u in oldfront):
                        yield u
        return set(g())

def main():
    farm = Farm(inpath().read_text().splitlines())
    oldfront = set()
    front = {farm.start}
    n = 0
    steps = 26501365
    r = range(steps, -1, -2)
    for i in range(steps + 1):
        if i in r:
            n += len(front)
        oldfront, front = front, farm.newfront(oldfront, front)
    print(n)
