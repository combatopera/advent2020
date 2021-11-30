#!/usr/bin/env python3

from pathlib import Path

kernel = [(x, y, z, w) for r in [range(-1, 2)] for x in r for y in r for z in r for w in r if x or y or z or w]

def vadd(u, v):
    return tuple(u[i]+v[i] for i in range(4))

def main():
    active = set()
    with Path('input', '17').open() as f:
        for y, l in enumerate(f):
            for x, c in enumerate(l.rstrip()):
                if '#' == c:
                    active.add((x, y, 0, 0))
    for _ in range(6):
        newactive = set()
        candidates = set()
        for cube in active:
            halo = [vadd(cube, k) for k in kernel]
            if sum(1 for c in halo if c in active) in {2, 3}:
                newactive.add(cube)
            candidates.update(c for c in halo if c not in active)
        for cube in candidates:
            if sum(1 for k in kernel if vadd(cube, k) in active) == 3:
                newactive.add(cube)
        active = newactive
    print(len(active))

if '__main__' == __name__:
    main()
