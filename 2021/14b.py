#!/usr/bin/env python3

from adventlib import readchunks
from collections import Counter
from itertools import islice
from pathlib import Path

class Template:

    @classmethod
    def compile(cls, text):
        d = Counter()
        d[text[0]] = d[text[-1]] = 1
        for a, b in zip(text, islice(text, 1, None)):
            d[a + b] += 1
        return cls(d)

    def __init__(self, d):
        self.d = d

    def insert(self, rules):
        d = Counter()
        for r, n in self.d.items():
            try:
                c = rules[r]
            except KeyError:
                d[r] += n
            else:
                d[r[0] + c] += n
                d[c + r[1]] += n
        return type(self)(d)

    def answer(self):
        d = Counter()
        for r, n in self.d.items():
            for c in r:
                d[c] += n
        for n in d.values():
            assert not n & 1
        return (max(d.values()) - min(d.values())) // 2

def main():
    with Path('input', '14').open() as f:
        (template,), rules = readchunks(f)
    template = Template.compile(template)
    rules = {x: y for x, _, y in (r.split() for r in rules)}
    for _ in range(40):
        template = template.insert(rules)
    print(template.answer())

if '__main__' == __name__:
    main()
