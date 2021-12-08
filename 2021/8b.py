#!/usr/bin/env python3

from itertools import permutations
from pathlib import Path

class Figure(frozenset):

    @classmethod
    def parse(cls, text):
        lines = [l for l in text.splitlines() if l]
        for digit in range(10):
            digittext = ''.join(l[3 * digit:3 * (digit + 1)] for l in lines)
            assert {' '} == set(digittext[::2])
            yield cls(i for i in range(7) if digittext[1 + 2 * i] != ' ')

class Patch:

    def __init__(self, chartosegment):
        self.chartosegment = chartosegment

    def _patches(self, pattern, figure):
        if len(figure) != len(pattern):
            return
        knownsegments = {i for c in pattern for i in [self.chartosegment.get(c)] if i is not None}
        if not knownsegments <= figure:
            return
        unknownsegments = list(figure - knownsegments)
        unknownchars = [c for c in pattern if c not in self.chartosegment]
        for chars in permutations(unknownchars):
            yield type(self)(dict(zip(chars, unknownsegments), **self.chartosegment))

    def search(self, patterns, figures):
        if patterns:
            for f in figures:
                for q in self._patches(patterns[0], f):
                    yield from q.search(patterns[1:], figures - {f})
        else:
            yield self

    def _decodeone(self, pattern):
        return figures[Figure(self.chartosegment[c] for c in pattern)]

    def decode(self, patterns):
        return sum(10 ** i * self._decodeone(p) for i, p in enumerate(reversed(patterns)))

emptypatch = Patch({})
figures = {f: digit for digit, f in enumerate(Figure.parse('''
 -     -  -     -  -  -  -  - $
| |  |  |  || ||  |    || || |$
       -  -  -  -  -     -  - $
| |  ||    |  |  || |  || |  |$
 -     -  -     -  -     -  - $
'''))}

def main():
    n = 0
    with Path('input', '8').open() as f:
        for line in f:
            patterns, digits = (s.split() for s in line.split('|'))
            patch, = emptypatch.search(sorted(patterns, key = lambda p: len(p)), figures.keys())
            n += patch.decode(digits)
    print(n)

if '__main__' == __name__:
    main()
