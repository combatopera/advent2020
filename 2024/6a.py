from adventlib import readgrid, Ring

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
                yield p
                guard = p

def main():
    grid = {}
    for p, c in readgrid():
        grid[p] = c
        if '^' == c:
            guard = p
            d = Ring([(0, -1), (1, 0), (0, 1), (-1, 0)])
    print(len(set(Walker(grid).walk(guard, d))))
