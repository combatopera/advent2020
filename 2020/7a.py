from adventlib import BagRule
from collections import defaultdict
from itertools import chain
from adventlib import inpath

def main():
    colortocontainers = defaultdict(set)
    with inpath().open() as f:
        for r in BagRule.readmany(f):
            for c in r.rhs:
                colortocontainers[c].add(r.lhs)
    nextcontainers = colortocontainers['shiny gold']
    containers = set()
    while nextcontainers:
        containers.update(nextcontainers)
        nextcontainers = set(chain(*(colortocontainers[c] for c in nextcontainers)))
    print(len(containers))
