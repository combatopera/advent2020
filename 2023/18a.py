from adventlib import inpath, Vector

dirs = dict(U = Vector([0, -1]), D = Vector([0, 1]), L = Vector([-1, 0]), R = Vector([1, 0]))

class Lagoon:

    def __init__(self):
        self.digger = Vector([0, 0])
        self.trench = set()

    def dig(self, instructions):
        for i in instructions:
            dir, n, _ = i.split()
            dir = dirs[dir]
            for _ in range(int(n)):
                self.digger += dir
                self.trench.add(self.digger)

    def capacity(self):
        def explore(p):
            tasks = [p]
            while tasks:
                p = tasks.pop()
                if p not in self.trench and p not in void:
                    void.add(p)
                    tasks.extend(p + d for d in dirs.values())
        minx = min(p[0] for p in self.trench)
        maxx = max(p[0] for p in self.trench)
        miny = min(p[1] for p in self.trench)
        maxy = max(p[1] for p in self.trench)
        void = set()
        for x in range(minx, maxx + 1):
            void.add((x, miny - 1))
            void.add((x, maxy + 1))
        for y in range(miny, maxy + 1):
            void.add((minx - 1, y))
            void.add((maxx + 1, y))
        boundary = len(void)
        for x in range(minx, maxx + 1):
            explore(Vector([x, miny]))
            explore(Vector([x, maxy]))
        for y in range(miny, maxy + 1):
            explore(Vector([minx, y]))
            explore(Vector([maxx, y]))
        return (maxx - minx + 1) * (maxy - miny + 1) - (len(void) - boundary)

def main():
    l = Lagoon()
    l.dig(inpath().read_text().splitlines())
    print(l.capacity())
