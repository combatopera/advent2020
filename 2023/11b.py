from adventlib import inpath, Vector
from itertools import islice

def main():
    galaxies = []
    for y, l in enumerate(inpath().read_text().splitlines()):
        for x, c in enumerate(l):
            if '#' == c:
                galaxies.append(Vector([x, y]))
    h = y + 1
    w = x + 1
    fatrows = set(range(h))
    fatcols = set(range(w))
    for g in galaxies:
        fatrows.discard(g[1])
        fatcols.discard(g[0])
    def manhattans():
        for i, g in enumerate(galaxies):
            for h in islice(galaxies, i + 1, None):
                n = 0
                for x in range(min(g[0], h[0]) + 1, max(g[0], h[0]) + 1):
                    n += 1 + (x in fatcols) * 999999
                for y in range(min(g[1], h[1]) + 1, max(g[1], h[1]) + 1):
                    n += 1 + (y in fatrows) * 999999
                yield n
    print(sum(manhattans()))
