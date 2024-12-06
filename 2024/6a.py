from adventlib import readgrid

class Ring:

    i = 0

    def __init__(self, v):
        self.v = v

    def _plus(self, k):
        return (self.i + k) % len(self.v)

    def step(self, k):
        self.i = self._plus(k)

    def __getitem__(self, k):
        return self.v[self._plus(k)]

class Walker:

    def __init__(self, grid):
        self.grid = grid

    def walk(self, guard, d):
        while True:
            p = guard + d[0]
            c = self.grid.get(p)
            if c is None:
                break
            if '#' == c:
                d.step(1)
            else:
                guard = p
                yield p

def main():
    grid = {}
    for p, c in readgrid():
        grid[p] = c
        if '^' == c:
            guard = p
            d = Ring([(0, -1), (1, 0), (0, 1), (-1, 0)])
    print(len(set(Walker(grid).walk(guard, d))))
