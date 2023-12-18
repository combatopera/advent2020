from adventlib import inpath, Vector
from collections import deque
import re

dirs = dict(U = Vector([0, -1]), D = Vector([0, 1]), L = Vector([-1, 0]), R = Vector([1, 0]))

def zones(vals):
    v = []
    for x in sorted(set(vals)):
        if v and v[-1].stop < x:
            v.append(range(v[-1].stop, x))
        v.append(range(x, x + 1))
    return v

class Lagoon:

    def __init__(self):
        self.digger = Vector([0, 0])
        self.trench = set()

    def dig(self, instructions):
        segments = []
        dirmap = {str(i): dirs[k] for i, k in enumerate('RDLU')}
        for i in instructions:
            h = re.search('[0-9a-f]{6}', i).group()
            n = int(h[:5], 16)
            d = dirmap[h[5]]
            segments.append([self.digger + d, self.digger + d * n])
            self.digger = segments[-1][1]
        self.xzones = zones(p[0] for s in segments for p in s)
        self.yzones = zones(p[1] for s in segments for p in s)
        def g():
            for p, q in segments:
                x1, = (i for i, x in enumerate(self.xzones) if p[0] in x)
                y1, = (i for i, y in enumerate(self.yzones) if p[1] in y)
                x2, = (i for i, x in enumerate(self.xzones) if q[0] in x)
                y2, = (i for i, y in enumerate(self.yzones) if q[1] in y)
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        yield x, y
        self.trench = set(g())

    def capacity(self):
        def explore(p):
            tasks = deque([p])
            while tasks:
                p = tasks.popleft()
                if not (p in void or p in boundary or p in self.trench):
                    void.add(p)
                    tasks.extend(p + d for d in dirs.values())
        boundary = set()
        for x, _ in enumerate(self.xzones):
            boundary.add((x, -1))
            boundary.add((x, len(self.yzones)))
        for y, _ in enumerate(self.yzones):
            boundary.add((-1, y))
            boundary.add((len(self.xzones), y))
        void = set()
        for x, _ in enumerate(self.xzones):
            explore(Vector([x, 0]))
            explore(Vector([x, len(self.yzones) - 1]))
        for y, _ in enumerate(self.yzones):
            explore(Vector([0, y]))
            explore(Vector([len(self.xzones) - 1, y]))
        return sum(map(len, self.xzones)) * sum(map(len, self.yzones)) - sum(len(self.xzones[x]) * len(self.yzones[y]) for x, y in void)

def main():
    l = Lagoon()
    l.dig(inpath().read_text().splitlines())
    print(l.capacity())
