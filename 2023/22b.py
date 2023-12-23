from adventlib import inpath

def intersects(p1, q1, p2, q2):
    return q1 >= p2 and p1 <= q2

class Brick:

    lowest = False

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
    def dropone():
        for i, b in enumerate(v):
            if b.lowest:
                continue
            floor = max((other.q[2] for other in b.below), default = 0)
            dz = b.p[2] - floor - 1
            if dz <= 0:
                continue
            b.drop(dz)
            if all(other.lowest for other in b.below):
                b.lowest = True
            return True
    v = sorted(bricks, key = lambda b: len(b.below))
    while dropone():
        pass

def reaction(bricks, drop):
    dropped = {drop}
    while True:
        more = {b for b in bricks if b not in dropped and b.supportedby and b.supportedby <= dropped}
        if not more:
            return len(dropped) - 1
        for b in more:
            dropped.add(b)

def main():
    bricks = [Brick.read(l) for l in inpath().read_text().splitlines()]
    for b in bricks:
        b.below = {other for other in bricks if other.q[2] < b.p[2] and other.samecol(b)}
    drop(bricks)
    for b in bricks:
        b.supports = {other for cap in [b.cap()] for other in bricks if other.intersects(cap)}
    for b in bricks:
        b.supportedby = {other for other in bricks if b in other.supports}
    print(sum(reaction(bricks, b) for b in bricks))
