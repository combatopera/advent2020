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

    def param(self, a):
        return self.p + a * self.v

def main():
    stones = []
    for l in inpath().read_text().splitlines():
        p, v = l.split('@')
        p = np.fromiter(map(int, p.split(',')), float)[:2]
        v = np.fromiter(map(int, v.split(',')), float)[:2]
        stones.append(Stone(p, v))
    n = 0
    for i, s in enumerate(stones):
        for t in islice(stones, i + 1, None):
            try:
                m = inv(np.array([[s.v[0], -t.v[0]], [s.v[1], -t.v[1]]]))
            except LinAlgError:
                continue
            a, b = m.dot(t.p - s.p)
            if a >=0 and b >= 0:
                p = s.param(a)
                if p[0] >= lo and p[0] <= hi and p[1] >= lo and p[1] <= hi:
                    n += 1
    print(n)
