#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path

def main():
    sums = defaultdict(int)
    n = 0
    with Path('input', '3').open() as f:
        for line in f:
            for i, c in enumerate(line.rstrip()):
                sums[i] += ord(c)
            n += 1
    threshold = sum(ord(c) for c in '01') * n / 2
    g = sum((x > threshold) * (1 << (len(sums) - i - 1)) for i, x in sums.items())
    e = sum((x < threshold) * (1 << (len(sums) - i - 1)) for i, x in sums.items())
    print(g * e)

if '__main__' == __name__:
    main()
