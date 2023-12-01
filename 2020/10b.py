from adventlib import differentiate, inpath
from functools import lru_cache, reduce
import operator, re

@lru_cache()
def runarrangements(adapters):
    def g():
        if adapters:
            for runarrangement in runarrangements(adapters - 1):
                yield 0 # Do not skip another adapter, reset skipped adapter counter.
                if runarrangement < 2: # If we haven't skipped 2 adjacent adapters, we can skip another.
                    yield runarrangement + 1 # Skip another adapter, increment counter.
        else:
            yield 0 # There is one possible arrangement of no adapters, in which none skipped.
    return list(g())

def main():
    with inpath().open() as f:
        joltages = [int(l) for l in f]
    joltages.append(max(joltages) + 3)
    joltages.append(0)
    joltages.sort()
    diffs = differentiate(joltages)
    assert 2 not in diffs # Convenient!
    print(reduce(operator.mul, (len(runarrangements(len(run) - 1)) for run in re.findall('1+', ''.join(map(str, diffs))))))
