from adventlib import inpath, Vector
from itertools import islice
from math import lcm
import re

class Moon:

    def __init__(self, p):
        self.p = p
        self.v = Vector([0, 0, 0])

    def attract(self, that):
        pull = [0] * 3
        for axis in range(3):
            if self.p[axis] != that.p[axis]:
                pull[axis] = (self.p[axis] < that.p[axis]) * 2 - 1
        self.v += pull
        that.v -= pull

    def accel(self):
        self.p += self.v

def main():
    def report(axis):
        return sum(((m.p[axis], m.v[axis]) for m in moons), ())
    moons = [Moon(Vector(map(int, re.findall('[0-9-]+', l)))) for l in inpath().read_text().splitlines()]
    n = 0
    initial = {a: report(a) for a in range(3)}
    periods = {}
    while len(periods) < 3:
        for i, m1 in enumerate(moons):
            for m2 in islice(moons, i + 1, None):
                m1.attract(m2)
        for m in moons:
            m.accel()
        n += 1
        for a in range(3):
            if a not in periods and report(a) == initial[a]:
                periods[a] = n
    print(lcm(*periods.values()))
