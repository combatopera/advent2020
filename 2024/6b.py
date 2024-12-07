from adventlib import readgrid, Ring
from itertools import islice

class Walker:

    def __init__(self, grid):
        self.grid = grid

    def walk(self, guard, facing):
        ring = Ring([(0, -1), (1, 0), (0, 1), (-1, 0)]).iadd(facing)
        while True:
            yield guard, ring
            p = guard + ring[0]
            c = self.grid.get(p)
            if c is None:
                break
            if '#' == c:
                ring.iadd(1)
            else:
                guard = p

class Obstructions:

    def __init__(self, grid):
        self.grid = grid

    def _checkobstruction(self, mainfootprint, guard, facing, obs):
        if '.' == self.grid.get(obs) and all((obs, i) not in mainfootprint for i in range(4)):
            footprint = mainfootprint.copy()
            for g, r in islice(Walker({**self.grid, obs: '#'}).walk(guard, facing), 1, None):
                if (g, r.index) in footprint:
                    return True
                footprint.add((g, r.index))

    def walk(self, guard, facing):
        footprint = set()
        obstructions = set()
        for g, r in Walker(self.grid).walk(guard, facing):
            footprint.add((g, r.index))
            obs = g + r[0]
            if obs not in obstructions and self._checkobstruction(footprint, g, r.index, obs):
                obstructions.add(obs)
        return len(obstructions)

def main():
    grid = {}
    for p, c in readgrid():
        grid[p] = c
        if '^' == c:
            guard = p
    print(Obstructions(grid).walk(guard, 0))
