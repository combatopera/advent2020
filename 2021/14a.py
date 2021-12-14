#!/usr/bin/env python3

from adventlib import readchunks
from collections import defaultdict
from itertools import islice
from pathlib import Path

class Rules:

    def __init__(self, rules):
        self.rules = rules

    def insert(self, template):
        for a, b in zip(template, islice(template, 1, None)):
            yield a
            yield self.rules[a + b]
        yield template[-1]

def main():
    with Path('input', '14').open() as f:
        (template,), rules = readchunks(f)
    rules = Rules({x: y for x, _, y in (r.split() for r in rules)})
    for _ in range(10):
        template = list(rules.insert(template))
    d = defaultdict(int)
    for c in template:
        d[c] += 1
    print(max(d.values()) - min(d.values()))

if '__main__' == __name__:
    main()
