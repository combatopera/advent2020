#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path

def _decode(patterns, digits):
    patterns = [set(p) for p in patterns]
    def take(l):
        p, = (p for p in patterns if l(p))
        patterns.remove(p)
        return p
    def pop():
        pop = defaultdict(int)
        for p in patterns:
            for c in p:
                pop[c] += 1
        return pop
    one = take(lambda p: len(p) == 2)
    four = take(lambda p: len(p) == 4)
    seven = take(lambda p: len(p) == 3)
    eight = take(lambda p: len(p) == 7)
    bl, = (c for c, n in pop().items() if n == 3)
    two = take(lambda p: len(p) == 5 and bl in p)
    nine = eight - {bl}
    patterns.remove(nine)
    five, = (p for p in patterns if bl not in p and p|{bl} in patterns)
    patterns.remove(five)
    six = five|{bl}
    patterns.remove(six)
    zero = take(lambda p: len(p) == 6)
    three, = patterns
    lookup = {frozenset(s): n for s, n in [
        [zero, 0],
        [one, 1],
        [two, 2],
        [three, 3],
        [four, 4],
        [five, 5],
        [six, 6],
        [seven, 7],
        [eight, 8],
        [nine, 9],
    ]}
    digits = [lookup[frozenset(d)] for d in digits]
    return int(''.join(str(d) for d in digits))

def main():
    n = 0
    with Path('input', '8').open() as f:
        for line in f:
            n += _decode(*(s.split() for s in line.split('|')))
    print(n)

if '__main__' == __name__:
    main()
