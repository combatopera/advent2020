#!/usr/bin/env python3

from itertools import islice
from pathlib import Path

def differentiate(v):
    return [y - x for x, y in zip(v, islice(v, 1, None))]

def main():
    with Path('input', '10').open() as f:
        joltages = [int(l) for l in f]
    joltages.append(max(joltages) + 3)
    joltages.append(0)
    joltages.sort()
    diffs = differentiate(joltages)
    print(diffs.count(1) * diffs.count(3))

if '__main__' == __name__:
    main()
