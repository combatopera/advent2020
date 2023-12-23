from adventlib import inpath
from itertools import chain

def intersects(p1, q1, p2, q2):
    return q1 >= p2 and p1 <= q2

class Brick:

    @classmethod
    def read(cls, l):
        p, q = l.split('~')
        p = list(map(int, p.split(',')))
        q = list(map(int, q.split(',')))
        for i in range(3):
            assert p[i] <= q[i]
        return cls(p, q)

    @classmethod
    def _of(cls, *args):
        return cls(*args)

    def __init__(self, p, q):
        self.supportedby = []
        self.supports = []
        self.p = p
        self.q = q

    def drop(self, dz):
        self.p[2] -= dz
        self.q[2] -= dz

    def samecol(self, that):
        return all(intersects(self.p[i], self.q[i], that.p[i], that.q[i]) for i in range(2))

    def intersects(self, that):
        return all(intersects(self.p[i], self.q[i], that.p[i], that.q[i]) for i in range(3))

    def cap(self):
        z = self.q[2] + 1
        return self._of([self.p[0], self.p[1], z], [self.q[0], self.q[1], z])

def drop(bricks):
    while True:
        bestdz = 0
        for b in bricks:
            floor = max(chain([0], (other.q[2] for other in bricks if other.q[2] < b.p[2] and b.samecol(other))))
            dz = b.p[2] - floor - 1
            if dz > bestdz:
                bestdz = dz
                bestbrick = b
        if not bestdz:
            break
        print(bestbrick, bestdz)
        bestbrick.drop(bestdz)

def main():
    bricks = [Brick.read(l) for l in inpath().read_text().splitlines()]
    drop(bricks)
    for b in bricks:
        cap = b.cap()
        for other in bricks:
            if other.intersects(cap):
                b.supports.append(other)
    for b in bricks:
        for other in bricks:
            if b in other.supports:
                b.supportedby.append(other)
    print(sum(1 for b in bricks if all([b] != other.supportedby for other in b.supports)))
