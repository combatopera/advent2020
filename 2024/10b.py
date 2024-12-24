from adventlib import readgrid
from diapyr.util import bfs

plus = (1, 0), (0, 1), (-1, 0), (0, -1)

def main():
    def score(p):
        @bfs([((), p)])
        def proc(info, k):
            discriminator, p = k
            n = info.depth + 1
            for i, d in enumerate(plus):
                q = p + d
                if grid.get(q) == n:
                    yield tuple([*discriminator, i]), q
        return len(proc.currentkeys) if 9 == proc.depth else 0
    grid = {}
    for p, c in readgrid():
        grid[p] = int(c)
    print(sum(score(p) for p, c in grid.items() if not c))
