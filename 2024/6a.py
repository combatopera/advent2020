from adventlib import readgrid, Ring

class Walker:

    def __init__(self, grid):
        self.grid = grid

    def walk(self, guard, facing):
        ring = Ring([(0, -1), (1, 0), (0, 1), (-1, 0)]).iadd(facing)
        while True:
            yield guard
            p = guard + ring[0]
            c = self.grid.get(p)
            if c is None:
                break
            if '#' == c:
                ring.iadd(1)
            else:
                guard = p

def main():
    grid = {}
    for p, c in readgrid():
        grid[p] = c
        if '^' == c:
            guard = p
    print(len(set(Walker(grid).walk(guard, 0))))
