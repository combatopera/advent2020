#!/usr/bin/env python3

from adventlib import readchunks, Vector
from pathlib import Path

def _getmap(u, v):
    (a, i), = ([a, i] for i in range(3) for a in [-1, 1] if a * u[i] == v[0])
    (b, j), = ([a, i] for i in range(3) for a in [-1, 1] if a * u[i] == v[1])
    (c, k), = ([a, i] for i in range(3) for a in [-1, 1] if a * u[i] == v[2])
    return lambda u: Vector([a * u[i], b * u[j], c * u[k]])

class Scanner:

    def __init__(self, beacons):
        self.characters = [{tuple(sorted(map(abs, b - o))): b for b in beacons} for o in beacons]
        assert all(len(c) == len(beacons) for c in self.characters)
        self.beacons = beacons

    def reorient(self, that):
        for c in self.characters:
            for d in that.characters:
                keys = c.keys() & d.keys()
                if len(keys) >= 12:
                    co = c[0, 0, 0]
                    do = d[0, 0, 0]
                    for k in keys:
                        if any(k):
                            m = _getmap(c[k] - co, d[k] - do)
                            break
                    assert {k: d[k] for k in keys} == {k: m(c[k]-co)+do for k in keys}
                    self.beacons = [m(b - co) + do for b in self.beacons]
                    return True

def main():
    with Path('input', '19').open() as f:
        scanners = [Scanner([Vector(map(int, p.split(','))) for p in chunk[1:]]) for chunk in readchunks(f)]
    oriented = {scanners[0]}
    while True:
        toorient = [s for s in scanners if s not in oriented]
        if not toorient:
            break
        oriented_ = set()
        for s in toorient:
            for t in oriented:
                if s.reorient(t):
                    oriented_.add(s)
                    break
        oriented |= oriented_
    from collections import Counter
    c = Counter()
    for s in scanners:
        for b in s.beacons:
            c[b] += 1
    print(len(c))

if '__main__' == __name__:
    main()
