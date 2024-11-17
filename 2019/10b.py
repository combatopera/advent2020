from adventlib import inpath, Vector
from collections import defaultdict
from math import gcd

def _order(u):
    x, y = u
    return x < 0, y / x if x else float('inf') * y

def main():
    def g():
        for a in asteroids:
            vectors = defaultdict(list)
            for other in asteroids:
                if other != a:
                    u = other - a
                    vectors[u / gcd(*u)].append(u)
            yield len(vectors), a, vectors
    asteroids = [Vector([x, y]) for y, l in enumerate(inpath().read_text().splitlines()) for x, c in enumerate(l) if '#' == c]
    _, station, vectors = max(g())
    for l in vectors.values():
        l.sort(key = lambda u: u[0] ** 2 + u[1] ** 2)
    dirs = sorted(vectors, key = _order)
    n = 0
    while True:
        for d in dirs:
            l = vectors[d]
            if l:
                u = l.pop(0)
                n += 1
                if 200 == n:
                    u += station
                    print(u[0] * 100 + u[1])
                    return
