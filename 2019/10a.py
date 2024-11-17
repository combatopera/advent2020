from adventlib import inpath, Vector
from math import gcd

def main():
    def g():
        for a in asteroids:
            vectors = set()
            for other in asteroids:
                if other != a:
                    u = other - a
                    vectors.add(u / gcd(*u))
            yield len(vectors)
    asteroids = [Vector([x, y]) for y, l in enumerate(inpath().read_text().splitlines()) for x, c in enumerate(l) if '#' == c]
    print(max(g()))
