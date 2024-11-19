from adventlib import inpath, Vector
from itertools import islice
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

    def energy(self):
        return sum(map(abs, self.p)) * sum(map(abs, self.v))

def main():
    moons = [Moon(Vector(map(int, re.findall('[0-9-]+', l)))) for l in inpath().read_text().splitlines()]
    for _ in range(1000):
        for i, m1 in enumerate(moons):
            for m2 in islice(moons, i + 1, None):
                m1.attract(m2)
        for m in moons:
            m.accel()
    print(sum(m.energy() for m in moons))
