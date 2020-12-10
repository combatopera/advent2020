#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path

def main():
    with Path('input', '10').open() as f:
        adapters = [int(l) for l in f]
    adapters.sort()
    adapters.append(max(adapters) + 3)
    counts = defaultdict(int)
    joltage = 0
    for a in adapters:
        counts[a - joltage] += 1
        joltage = a
    assert counts.keys() <= {1, 2, 3}
    print(counts[1] * counts[3])

if '__main__' == __name__:
    main()
