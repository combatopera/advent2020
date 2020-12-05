#!/usr/bin/env python3

from pathlib import Path

xform = dict(F = 0, B = 1, L = 0, R = 1)
size = 10
factors = [2 ** i for i in range(size)]
factors.reverse()

def main():
    space = range(2 ** size)
    seats = set(space)
    with Path('input', '5').open() as f:
        for l in f:
            seats.remove(sum(f * xform[l[i]] for i, f in enumerate(factors)))
    try:
        for s in space:
            seats.remove(s)
    except KeyError:
        print(min(seats))

if '__main__' == __name__:
    main()
