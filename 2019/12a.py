from adventlib import inpath, Vector
import re

class Moon:

    def __init__(self, p):
        self.p = p
        self.v = Vector([0, 0, 0])

    def energy(self):
        return sum(map(abs, self.p)) * sum(map(abs, self.v))

def main():
    moons = [Moon(Vector(map(int, re.findall('[0-9-]+', l)))) for l in inpath().read_text().splitlines()]
    for _ in range(1000):
        pass
    print(sum(m.energy() for m in moons))
