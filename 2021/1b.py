#!/usr/bin/env python3

from itertools import islice
from pathlib import Path

def main():
    v = list(map(int, Path('input', '1').read_text().splitlines()))
    w = sum(islice(v, 3))
    n = 0
    for x, y in zip(v, islice(v, 3, None)):
        w_ = w - x + y
        n += w < w_
        w = w_
    print(n)

if '__main__' == __name__:
    main()
