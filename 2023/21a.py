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
        self.w = x + 1
        self.h = y + 1
        for x in range(self.w):
            self.rocks.add((x, -1))
            self.rocks.add((x, self.h))
        for y in range(self.h):
            self.rocks.add((-1, y))
            self.rocks.add((self.w, y))

    def newfront(self, oldfront, front):
        def g():
            for t in front:
                for d in dirs:
                    u = t + d
                    if not (u in self.rocks or u in oldfront):
                        yield u
        return set(g())

def main():
    farm = Farm(inpath().read_text().splitlines())
    oldfront = set()
    front = {farm.start}
    total = 0
    steps = 64
    sieve = range(steps, -1, -2)
    step = 0
    while True:
        if step in sieve:
            total += len(front)
        if step == steps:
            break
        step += 1
        oldfront, front = front, farm.newfront(oldfront, front)
    print(total)
