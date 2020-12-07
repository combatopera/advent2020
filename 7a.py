#!/usr/bin/env python3

from adventlib import BagRule
from collections import defaultdict
from itertools import chain
from pathlib import Path

def main():
    colortocontainers = defaultdict(set)
    with Path('input', '7').open() as f:
        for r in BagRule.readmany(f):
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
