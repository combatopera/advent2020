from adventlib import inpath
from itertools import islice
from numpy.linalg import inv, LinAlgError
import numpy as np

lo = 200000000000000
hi = 400000000000000

class Stone:

    def __init__(self, p, v):
        self.p = p
        self.v = v

    def intersect(self, that):
        try:
            m = inv(np.array([[self.v[0], -that.v[0]], [self.v[1], -that.v[1]]]))
        except LinAlgError:
            return
        a, b = m.dot(that.p - self.p)
        if a >= 0 and b >= 0:
            return a

    def param(self, t):
        return self.p + t * self.v

def main():
    stones = []
    for l in inpath().read_text().splitlines():
        p, v = l.split('@')
        p = np.fromiter(islice(map(int, p.split(',')), 2), float)
        v = np.fromiter(islice(map(int, v.split(',')), 2), float)
        stones.append(Stone(p, v))
    n = 0
    for i, s in enumerate(stones):
        for t in islice(stones, i + 1, None):
            a = s.intersect(t)
            if a is not None:
                p = s.param(a)
                if p[0] >= lo and p[0] <= hi and p[1] >= lo and p[1] <= hi:
                    n += 1
    print(n)
