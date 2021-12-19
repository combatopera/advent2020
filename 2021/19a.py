#!/usr/bin/env python3

from adventlib import readchunks, Vector
from pathlib import Path

class Scanner:

    def __init__(self, points):
        self.characters = [{tuple(sorted(map(abs, p - com))): p for p in points} for com in points]
        assert all(len(c) == len(points) for c in self.characters)
        self.points = points

    def reorient(self, that):
        def match():
            for c in self.characters:
                for d in that.characters:
                    if len(c.keys() & d.keys()) >= 12:
                        return True
        if not match():
            return
        ...
        return True

def main():
    with Path('input', '19').open() as f:
        scanners = [Scanner([Vector(map(int, p.split(','))) for p in chunk[1:]]) for chunk in readchunks(f)]
    oriented = {scanners[0]}
    while True:
        toorient = [s for s in scanners if s not in oriented]
        if not toorient:
            break
        oriented |= {s for s in toorient for t in oriented if s.reorient(t)}

if '__main__' == __name__:
    main()
