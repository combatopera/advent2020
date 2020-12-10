#!/usr/bin/env python3

from adventlib import differentiate
from functools import reduce
from pathlib import Path
import operator, re

def factor(runsize):
    return min(7, 2 ** (runsize - 1))

def main():
    with Path('input', '10').open() as f:
        joltages = [int(l) for l in f]
    joltages.append(max(joltages) + 3)
    joltages.append(0)
    joltages.sort()
    diffs = differentiate(joltages)
    assert 2 not in diffs
    runs = [len(run) for run in re.findall('1+', ''.join(map(str, diffs)))]
    print(reduce(operator.mul, map(factor, runs)))

if '__main__' == __name__:
    main()
