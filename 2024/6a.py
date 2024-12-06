from adventlib import readgrid, Ring

class Walker:

    def __init__(self, grid):
        self.grid = grid

    def walk(self, guard, facing):
        ring = Ring([(0, -1), (1, 0), (0, 1), (-1, 0)])
        ring.step(facing)
        while True:
            p = guard + ring[0]
            c = self.grid.get(p)
            if c is None:
                break
            if '#' == c:
                ring.step(1)
            else:
                yield p
                guard = p

def main():
    grid = {}
    for p, c in readgrid():
        grid[p] = c
        if '^' == c:
            guard = p
    print(len({guard, *Walker(grid).walk(guard, 0)}))
