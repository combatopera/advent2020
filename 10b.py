#!/usr/bin/env python3

from adventlib import differentiate
from functools import lru_cache, reduce
from pathlib import Path
import operator, re

@lru_cache()
def runarrangements(runlen):
    def g():
        if 1 == runlen:
            yield 0
        else:
            for runarrangement in runarrangements(runlen - 1):
                yield 0
                if runarrangement < 2:
                    yield runarrangement + 1
    return list(g())

def main():
    with Path('input', '10').open() as f:
        joltages = [int(l) for l in f]
    joltages.append(max(joltages) + 3)
    joltages.append(0)
    joltages.sort()
    diffs = differentiate(joltages)
    assert 2 not in diffs
    print(reduce(operator.mul, (len(runarrangements(len(run))) for run in re.findall('1+', ''.join(map(str, diffs))))))

if '__main__' == __name__:
    main()
