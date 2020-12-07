#!/usr/bin/env python3

from collections import defaultdict
from itertools import chain
from pathlib import Path
import re

class Rule:

    outer = re.compile('(.+) bags contain (.+)[.]')
    inner = re.compile('([1-9]) (.+) bags?')

    def __init__(self, line):
        self.lhs, v = self.outer.fullmatch(line).groups()
        self.rhs = {} if 'no other bags' == v else {c: int(n) for x in v.split(', ') for n, c in [self.inner.fullmatch(x).groups()]}

def readrules():
    with Path('input', '7').open() as f:
        for l in f:
            yield Rule(l.rstrip())

def main():
    colortocontained = {}
    for r in readrules():
        colortocontained[r.lhs] = r.rhs
    def contains(color):
        return sum(n * (1 + contains(c)) for c, n in colortocontained[color].items())
    print(contains('shiny gold'))

if '__main__' == __name__:
    main()
