#!/usr/bin/env python3

from collections import defaultdict
from itertools import chain
from pathlib import Path
import re

class Rule:

    outer = re.compile('(.+) bags contain (.+)[.]')
    inner = re.compile('[1-9] (.+) bags?')

    def __init__(self, line):
        self.lhs, v = self.outer.fullmatch(line).groups()
        self.rhs = [] if 'no other bags' == v else [self.inner.fullmatch(x).group(1) for x in v.split(', ')]

def readrules():
    with Path('input', '7').open() as f:
        for l in f:
            yield Rule(l.rstrip())

def main():
    colortocontainers = defaultdict(set)
    for r in readrules():
        for c in r.rhs:
            colortocontainers[c].add(r.lhs)
    nextcontainers = colortocontainers['shiny gold']
    containers = set()
    while nextcontainers:
        containers.update(nextcontainers)
        nextcontainers = set(chain(*(colortocontainers[c] for c in nextcontainers)))
    print(len(containers))

if '__main__' == __name__:
    main()
