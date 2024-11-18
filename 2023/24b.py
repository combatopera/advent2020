from adventlib import inpath
from numpy.linalg import solve
import numpy as np

class Stone:

    def __init__(self, p, v):
        self.p = p
        self.v = v

    def param(self, t):
        return self.p + t * self.v

def main():
    def sample():
        for l in inpath().read_text().splitlines()[:5]:
            p, v = l.split('@')
            p = np.fromiter(map(int, p.split(',')), int)
            v = np.fromiter(map(int, v.split(',')), int)
            yield Stone(p, v)
    a, b, c, d, e = sample()
    matrix = np.array([
        [b.v[1] - a.v[1], a.v[0] - b.v[0], a.p[1] - b.p[1], b.p[0] - a.p[0]],
        [c.v[1] - a.v[1], a.v[0] - c.v[0], a.p[1] - c.p[1], c.p[0] - a.p[0]],
        [d.v[1] - a.v[1], a.v[0] - d.v[0], a.p[1] - d.p[1], d.p[0] - a.p[0]],
        [e.v[1] - a.v[1], a.v[0] - e.v[0], a.p[1] - e.p[1], e.p[0] - a.p[0]],
    ])
    const = np.array([
        a.p[1] * a.v[0] - a.p[0] * a.v[1] - b.p[1] * b.v[0] + b.p[0] * b.v[1],
        a.p[1] * a.v[0] - a.p[0] * a.v[1] - c.p[1] * c.v[0] + c.p[0] * c.v[1],
        a.p[1] * a.v[0] - a.p[0] * a.v[1] - d.p[1] * d.v[0] + d.p[0] * d.v[1],
        a.p[1] * a.v[0] - a.p[0] * a.v[1] - e.p[1] * e.v[0] + e.p[0] * e.v[1],
    ])
    px, py, vx, vy = solve(matrix, const)
    matrix = np.array([
        [b.v[2] - a.v[2], a.v[0] - b.v[0], a.p[2] - b.p[2], b.p[0] - a.p[0]],
        [c.v[2] - a.v[2], a.v[0] - c.v[0], a.p[2] - c.p[2], c.p[0] - a.p[0]],
        [d.v[2] - a.v[2], a.v[0] - d.v[0], a.p[2] - d.p[2], d.p[0] - a.p[0]],
        [e.v[2] - a.v[2], a.v[0] - e.v[0], a.p[2] - e.p[2], e.p[0] - a.p[0]],
    ])
    const = np.array([
        a.p[2] * a.v[0] - a.p[0] * a.v[2] - b.p[2] * b.v[0] + b.p[0] * b.v[2],
        a.p[2] * a.v[0] - a.p[0] * a.v[2] - c.p[2] * c.v[0] + c.p[0] * c.v[2],
        a.p[2] * a.v[0] - a.p[0] * a.v[2] - d.p[2] * d.v[0] + d.p[0] * d.v[2],
        a.p[2] * a.v[0] - a.p[0] * a.v[2] - e.p[2] * e.v[0] + e.p[0] * e.v[2],
    ])
    px, pz, vx, vz = solve(matrix, const)
    ta = round((a.p[0] - px) / (vx - a.v[0]))
    v = np.fromiter(map(round, [vx, vy, vz]), int)
    p = a.param(ta) - ta * v
    print(sum(p))
