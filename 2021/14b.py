#!/usr/bin/env python3

from adventlib import readchunks
from collections import defaultdict
from itertools import islice
from pathlib import Path

class Rules:

    def __init__(self, rules):
        self.rules = rules

    def compile(self, template):
        d = defaultdict(int)
        d[template[0]] = d[template[-1]] = 1
        for a, b in zip(template, islice(template, 1, None)):
            d[a + b] += 1
        return d

    def insert(self, template):
        d = defaultdict(int)
        for r, n in template.items():
            try:
                c = self.rules[r]
            except KeyError:
                d[r] += n
            else:
                d[r[0] + c] += n
                d[c + r[1]] += n
        return d

    def answer(self, template):
        d = defaultdict(int)
        for r, n in template.items():
            for c in r:
                d[c] += n
        for n in d.values():
            assert not n & 1
        return (max(d.values()) - min(d.values())) // 2

def main():
    with Path('input', '14').open() as f:
        (template,), rules = readchunks(f)
    rules = Rules({x: y for x, _, y in (r.split() for r in rules)})
    template = rules.compile(template)
    for _ in range(40):
        template = rules.insert(template)
    print(rules.answer(template))

if '__main__' == __name__:
    main()
