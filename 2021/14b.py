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
        d['$'+template[0]] = 1
        d['$'+template[-1]] = 1
        for a, b in zip(template, islice(template, 1, None)):
            d[a+b] += 1
        return d

    def insert(self, template):
        d = defaultdict(int)
        for r, n in template.items():
            if '$'!=r[0]:
                c = self.rules[r]
                d[r[0]+c] += n
                d[c+r[1]] += n
            else:
                d[r]+=n
        return d

    def answer(self, template):
        d = defaultdict(int)
        for r, n in template.items():
            if '$'==r[0]:
                d[r[1]]+=n/2
            else:
                for c in r:
                    d[c] += n/2
        return max(d.values()) - min(d.values())

def main():
    with Path('input', '14').open() as f:
        (template,), rules = readchunks(f)
    rules = Rules({x: y for x, _, y in (r.split() for r in rules)})


    print(template)
    template = rules.compile(template)
    print(template)




    for _ in range(40):
        template = rules.insert(template)
        #print(template)

        print(rules.answer(template))

if '__main__' == __name__:
    main()
