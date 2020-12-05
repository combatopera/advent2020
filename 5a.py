#!/usr/bin/env python3

from pathlib import Path

xform = dict(F = 0, B = 1, L = 0, R = 1)

def main():
    def g():
        with Path('input', '5').open() as f:
            for l in f:
                yield sum(2 ** i * xform[c] for i, c in enumerate(l[9::-1]))
    print(max(g()))

if '__main__' == __name__:
    main()
