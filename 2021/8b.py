#!/usr/bin/env python3

from itertools import permutations
from pathlib import Path

class Figure:

    def __init__(self, digit, segments):
        self.segments = {i for i, c in enumerate(segments) if c != ' '}
        self.digit = digit

figures = [
    Figure(0, '-|| ||-'),
    Figure(1, '  |  | '),
    Figure(2, '- |-| -'),
    Figure(3, '- |- |-'),
    Figure(4, ' ||- | '),
    Figure(5, '-| - |-'),
    Figure(6, '-| -||-'),
    Figure(7, '- |  | '),
    Figure(8, '-||-||-'),
    Figure(9, '-||- |-'),
]
figurelookup = {frozenset(f.segments): f for f in figures}

class Patch:

    def __init__(self, chartosegment):
        self.chartosegment = chartosegment

    def patches(self, figure, pattern):
        if len(figure.segments) != len(pattern):
            return
        knownsegments = {i for c in pattern for i in [self.chartosegment.get(c)] if i is not None}
        if not knownsegments <= figure.segments:
            return
        unknownsegments = list(figure.segments - knownsegments)
        unknownchars = [c for c in pattern if c not in self.chartosegment]
        for chars in permutations(unknownchars):
            yield type(self)(dict(self.chartosegment, **dict(zip(chars, unknownsegments))))

    def _decodeone(self, pattern):
        return figurelookup[frozenset(self.chartosegment[c] for c in pattern)].digit

    def decode(self, patterns):
        return sum(10 ** i * self._decodeone(p) for i, p in enumerate(reversed(patterns)))

def _patchrec(patterns, figures, patch):
    if patterns:
        for f in figures:
            for q in patch.patches(f, patterns[0]):
                yield from _patchrec(patterns[1:], figures - {f}, q)
    else:
        yield patch

def main():
    n = 0
    with Path('input', '8').open() as f:
        for line in f:
            patterns, digits = (s.split() for s in line.split('|'))
            patch, = _patchrec(sorted(patterns, key = lambda p: len(p)), set(figures), Patch({}))
            n += patch.decode(digits)
    print(n)

if '__main__' == __name__:
    main()
