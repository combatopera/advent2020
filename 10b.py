#!/usr/bin/env python3

from adventlib import differentiate
from functools import lru_cache, reduce
from pathlib import Path
import operator, re

@lru_cache()
def runarrangements(runlen):
    def g():
        if 1 == runlen:
            yield 0 # There are no adapters to skip.
        else:
            for runarrangement in runarrangements(runlen - 1):
                yield 0 # Do not skip another adapter, reset skipped adapter counter.
                if runarrangement < 2: # We can skip at most 2 adapters at a time.
                    yield runarrangement + 1 # Skip another adapter, increment counter.
    return list(g())

def main():
    with Path('input', '10').open() as f:
        joltages = [int(l) for l in f]
    joltages.append(max(joltages) + 3)
    joltages.append(0)
    joltages.sort()
    diffs = differentiate(joltages)
    assert 2 not in diffs # Convenient!
    print(reduce(operator.mul, (len(runarrangements(len(run))) for run in re.findall('1+', ''.join(map(str, diffs))))))

if '__main__' == __name__:
    main()
