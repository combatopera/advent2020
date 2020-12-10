#!/usr/bin/env python3

from functools import reduce
from itertools import islice
from pathlib import Path
import operator, re

def arrangements(runsize):
    return min(7, 2 ** (runsize - 1))

def main():
    joltages = [0]
    with Path('input', '10').open() as f:
        joltages.extend(int(l) for l in f)
    joltages.sort()
    print(joltages)
    diffs = ''.join(str(j1 - j0) for j0, j1 in zip(joltages, islice(joltages, 1, None)))
    print(diffs)
    runs = [len(run) for run in re.split('3+', diffs)]
    print(runs)
    factors = [arrangements(rs) for rs in runs]
    print(factors)
    print(reduce(operator.mul, factors))

if '__main__' == __name__:
    main()
