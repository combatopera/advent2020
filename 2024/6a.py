from adventlib import readgrid

dirs = (0, -1), (1, 0), (0, 1), (-1, 0)

class Walker:

    def __init__(self, grid):
        self.grid = grid

    def walk(self, guard, d):
        while True:
            p = guard + dirs[d]
            c = self.grid.get(p)
            if c is None:
                break
            if '#' == c:
                d = (d + 1) % len(dirs)
            else:
                guard = p
                yield p

def main():
    grid = {}
    for p, c in readgrid():
        grid[p] = c
        if '^' == c:
            guard = p
            d = 0
    footprint = set(Walker(grid).walk(guard, d))
    print(len(footprint))
