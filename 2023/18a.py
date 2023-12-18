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
        def explore(p, d):
            q = p + d
            if q not in self.trench and q not in void:
                void.add(q)
                for d in dirs.values():
                    explore(q, d)
        minx = min(p[0] for p in self.trench)
        endx = max(p[0] for p in self.trench) + 1
        miny = min(p[1] for p in self.trench)
        endy = max(p[1] for p in self.trench) + 1
        void = set()
        for x in range(minx, endx):
            void.add((x, -1))
            void.add((x, endy))
        for y in range(miny, endy):
            void.add((-1, y))
            void.add((endx, y))
        n = len(void)
        for x in range(minx, endx):
            explore(Vector([x, -1]), Vector([0, 1]))
            explore(Vector([x, endy]), Vector([0, -1]))
        for y in range(miny, endy):
            explore(Vector([-1, y]), Vector([1, 0]))
            explore(Vector([endx, y]), Vector([-1, 0]))
        return (endx - minx) * (endy - miny) - (len(void) - n)

def main():
    l = Lagoon()
    l.dig(inpath().read_text().splitlines())
    print(l.capacity())
