#!/usr/bin/env python3

from pathlib import Path

xform = dict(F = 0, B = 1, L = 0, R = 1)
size = 10

def main():
    space = range(2 ** size)
    seats = set(space)
    with Path('input', '5').open() as f:
        for l in f:
            seats.remove(sum(2 ** i * xform[c] for i, c in enumerate(l[size - 1::-1])))
    try:
        for s in space:
            seats.remove(s)
    except KeyError:
        print(min(seats))

if '__main__' == __name__:
    main()
